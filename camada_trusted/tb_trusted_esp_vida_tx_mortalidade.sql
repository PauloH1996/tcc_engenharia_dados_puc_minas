--legendas 
-- srs = series
-- cls = classificacoes

CREATE TABLE dados_trusted.tb_trusted_esp_vida_tx_mortalidade AS ( 

WITH separar_chaves AS ( 

SELECT elem->>'id' as id
	   , elem->>'unidade' as unidade 
	   , elem->>'variavel' as variavel
	   , CAST(elem->>'resultados' AS JSONB) as resultados   
FROM dados_raw.tb_raw_fecundidade,
	 jsonb_array_elements(data) AS elem 
),
	
abrindo_json_pt1 AS ( 
SELECT id 
	, unidade
	, variavel
	, CAST(elem->'series' AS JSONB) as series
	, CAST(elem->'classificacoes' AS JSONB) as classificacoes 
FROM separar_chaves, 
	 jsonb_array_elements(resultados) AS elem
),

abrindo_json_pt2 AS (
SELECT id 
	, unidade
	, variavel
	, CAST(elem_series->'serie' AS JSONB) as srs_serie
	, CAST(elem_series->'localidade' AS JSONB) as srs_localidade	
	, elem_classificacoes->>'id' as cls_id 
	, elem_classificacoes->>'nome' as cls_nome
	, CAST(elem_classificacoes->'categoria' AS JSONB) as cls_categoria
	
FROM abrindo_json_pt1, 
	 jsonb_array_elements(series) AS elem_series,
	 jsonb_array_elements(classificacoes) AS elem_classificacoes
),

tabela_final AS (
SELECT id 
	, unidade
	, variavel
	, '2018' as ano_pesquisa
	, srs_serie->>'2018' as srs_serie
	, srs_localidade->>'nome' as srs_localidade	
	, cls_id 
	, cls_nome
	, CAST((jsonb_each(cls_categoria)).value AS TEXT) as cls_categoria
	
FROM abrindo_json_pt2
)

	--Tabela final
SELECT id 
	, unidade
	, variavel
	, ano_pesquisa
	, srs_serie
	, srs_localidade	
	, cls_id 
	, cls_nome
	, substring(cls_categoria FROM 2 FOR length(cls_categoria) - 2) AS cls_categoria
FROM tabela_final 

) 
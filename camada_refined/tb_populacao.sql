--variavel = tabela refined  
--agregador = tabelas raw/trusted

CREATE TABLE dados_refined.tb_populacao AS (
WITH refinando_pt1 AS ( 
	SELECT *
	FROM dados_trusted.tb_trusted_populacao
	WHERE cls_nome = 'Ano'
),
refinando_pt2 AS (
	SELECT *
	FROM dados_trusted.tb_trusted_populacao
	WHERE cls_nome != 'Ano'	
)
--TABELA FINAL
SELECT CAST(pt1.id AS INTEGER) AS id
	, CAST(pt1.unidade AS TEXT) AS unidade
	, CAST(pt1.variavel AS TEXT) AS variavel
	, CAST(pt1.ano_pesquisa AS INTEGER) AS ano_pesquisa
	, CAST(pt1.srs_serie AS NUMERIC) AS indicador
	, CAST(pt1.srs_localidade AS TEXT) AS localidade
	, CAST(pt2.cls_id AS INTEGER) as cls_id_genero
	, CAST(pt2.cls_categoria AS TEXT) as cls_categoria_genero
	, CAST(pt1.cls_id AS INTEGER) as cls_id_ano_base
	, CAST(pt1.cls_categoria AS TEXT) as cls_categora_ano_base
FROM refinando_pt1 as pt1
INNER JOIN refinando_pt2 AS pt2
	ON pt1.id = pt2.id
	AND pt1.unidade = pt2.unidade
	AND pt1.variavel = pt2.variavel
	AND pt1.srs_serie = pt2.srs_serie
WHERE pt2.cls_categoria != 'Total'
	
) 
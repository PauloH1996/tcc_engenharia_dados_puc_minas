/*
Variavel  
"Óbitos"
"Idade mediana"
"Razão de dependência de jovens"
"Saldo migratório internacional"
"Nascimentos"
"Saldo migratório interno"
"Taxa bruta de mortalidade"
"Taxa bruta de natalidade"
"Taxa de crescimento geométrico"
"Índice de envelhecimento"
"Taxa de fecundidade total"
"Razão de dependência de idosos"
"Razão de dependência total"
"Taxa líquida de migração"
"Saldo migratório total"
*/

CREATE TABLE dados_refined.tb_indicadores_implicitos AS (

--TABELA FINAL
SELECT DISTINCT 
	  CAST(id AS INTEGER) AS id
	, CAST(unidade AS TEXT) AS unidade
	, CAST(variavel AS TEXT) AS variavel
	, CAST(ano_pesquisa AS INTEGER) AS ano_pesquisa
	, CAST(srs_serie AS TEXT) AS indicador
	, CAST(srs_localidade AS TEXT) AS localidade
	, CAST(cls_id AS INTEGER) as cls_id_ano_base
	, CAST(cls_categoria AS TEXT) as cls_categora_ano_base
FROM dados_trusted.tb_trusted_indicadores_implicitos
)

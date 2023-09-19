#Guia de gerador de tabelas

#primeira tabela 
#url= "https://servicodados.ibge.gov.br/api/v3/agregados/7362/periodos/2018/variaveis/2503|1940?localidades=N1[all]&classificacao=2[4,5]|1933[all]"
##7362- Esperança de vida ao nascer e Taxa de mortalidade infantil, por sexo
#segunda tabela  
#url= "https://servicodados.ibge.gov.br/api/v3/agregados/7360/periodos/2018/variaveis/10600|10601|10602|10603|10604|10605|10606|10607|10608|2493|10609|10610|10611|10612|10613?localidades=N1[all]&classificacao=1933[all]"
##7360- Indicadores implícitos na projeção da população
#terceira tabela  
#url= "https://servicodados.ibge.gov.br/api/v3/agregados/7358/periodos/2018/variaveis/606?localidades=N1[all]&classificacao=2[4,5]|287[100362]|1933[all]"
##7358- População, por sexo e idade
#quarta tabela  
#url= "https://servicodados.ibge.gov.br/api/v3/agregados/7365/periodos/2018/variaveis/10615?localidades=N1[all]&classificacao=58[all]|1933[all]"
##7365- Proporção de pessoas, por grupo de idade
#quinta tabela  
#url= "https://servicodados.ibge.gov.br/api/v3/agregados/7363/periodos/2018/variaveis/10614?localidades=N1[all]&classificacao=950[all]|1933[all]"
##7363- Taxa específica de fecundidade, por grupo de idade da mãe

import requests
import json
import pandas as pd

class IBGEQueryBuilder:
    def __init__(self, base_url):
        self.base_url = base_url

    def build_query(self):
        url = f"{self.base_url}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch data from IBGE API. Status code: {response.status_code}")

if __name__ == "__main__":
    # Definindo url de Esperança de vida ao nascer e Taxa de mortalidade infantil, por sexo conforme print .
    ibge_base_url = "https://servicodados.ibge.gov.br/api/v3/agregados/7363/periodos/2018/variaveis/10614?localidades=N1[all]&classificacao=950[all]|1933[all]"
    
    # Criando a instância IBGEQueryBuilder.
    ibge_query_builder = IBGEQueryBuilder(ibge_base_url)
    
    # Especificando a função de build_query para fazer validação de sucesso==200 ou espeficicar error
    ibge_data = ibge_query_builder.build_query()
    
    # Nome do arquivo onde você deseja salvar os dados JSON.
    nome_arquivo = json.dump(ibge_data)

    # Abra o arquivo no modo de escrita.
    #with open(nome_arquivo, "w") as arquivo_json:
    #    # Use json.dump() para escrever os dados no arquivo.
    #    json.dump(ibge_data, arquivo_json)
#
    #print(f"Os dados foram salvos em '{nome_arquivo}'.")
        #Transformando o resultado em dataframe

    df = pd.read_json(nome_arquivo)
    print(df.head())

   
    #primeira tabela 
    #tb_raw_esp_vida_tx_mortalidade
    #segunda tabela  
    #tb_raw_indicadores_implicitos 
    #terceira tabela  
    #tb_raw_populacao 
    #quarta tabela  
    #tb_raw_proporcao_pessoas 
    #quinta tabela  
    #tb_raw_fecundidade

    



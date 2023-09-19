import requests
import json
import pandas as pd


    
url = 'https://servicodados.ibge.gov.br/api/v3/agregados/7362/periodos/2018/variaveis/2503?localidades=N1[all]&classificacao=2[all]'
response = requests.get(url)



print(response)

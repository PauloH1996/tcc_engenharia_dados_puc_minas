import requests

def consultar_estados():
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
    response = requests.get(url)
    
    if response.status_code == 200:
        estados = response.json()
        for estado in estados:
            print(f"{estado['sigla']} - {estado['nome']}")
    else:
        print(f"Erro ao consultar a API: {response.status_code}")

def consultar_municipios_por_estado(estado_sigla):
    url = f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado_sigla}/municipios'
    response = requests.get(url)

    if response.status_code == 200:
        municipios = response.json()
        for municipio in municipios:
            print(municipio['nome'])
    else:
        print(f"Erro ao consultar a API: {response.status_code}")

# Consultar estados
print("Estados brasileiros:")
consultar_estados()

# Consultar municípios de um estado específico (no exemplo, São Paulo - SP)
print("\nMunicípios de São Paulo:")
consultar_municipios_por_estado('SP')

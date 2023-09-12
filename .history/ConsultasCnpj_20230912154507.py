import requests
import pandas as pd
import json
import time
  

# Função para consultar um CNPJ e retornar os dados em JSON
def consultar_cnpj(cnpj):
    url = f"https://publica.cnpj.ws/cnpj/{cnpj}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 429:
        # Lidar com a limitação de taxa, aguardar o tempo especificado na mensagem de erro
        wait_time = int(response.headers.get('Retry-After', 60))
        print(f'Limite de taxa atingido. Aguardando {wait_time} segundos...')
        time.sleep(wait_time)
        return consultar_cnpj(cnpj)  # Tentar novamente após a espera
    else:
        print(f'Erro ao consultar CNPJ {cnpj}: {response.status_code}')
        return None

# Ler a planilha XLSX com a lista de CNPJs
df = pd.read_excel('ListaCnpj.xlsx')

# Inicializar uma lista para armazenar os dados de todos os CNPJs
dados_cnpjs = []

# Loop através dos CNPJs e fazer as consultas
for cnpj in df['CNPJ']:
    dados = consultar_cnpj(cnpj)
    if dados:
        dados_cnpjs.append(dados)

# Salvar todos os dados em um único arquivo JSON
with open('dados_cnpjs.json', 'w', encoding='utf-8') as json_file:
    json.dump(dados_cnpjs, json_file, ensure_ascii=False, indent=4)

print(f'Dados de {len(dados_cnpjs)} CNPJs foram salvos em "dados_cnpjs.json".')



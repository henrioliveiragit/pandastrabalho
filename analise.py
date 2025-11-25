import pandas as pd
import os

#Precisei pegar o path do arquivo csv para funcionar
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "dados.csv")
dados_lidos = pd.read_csv(csv_path, sep=";")

print("====Informações gerais====")
print(dados_lidos.info()) 
print("\n====Estatísticas====")
print(dados_lidos.describe()) 

N = 5

print(f"\n====Primeiras {N} linhas====")
print(dados_lidos.head(N))  

print(f"\n====Últimas {N} linhas====")
print(dados_lidos.tail(N))  

nova_variavel = dados_lidos

nova_variavel['Calories'] = nova_variavel['Calories'].fillna(0)

print("\n====Conjunto de dados após substituição de valores nulos====")
print(nova_variavel)

nova_variavel['Date'] = nova_variavel['Date'].fillna('1900/01/01')

nova_variavel['Date'] = nova_variavel['Date'].replace('1900/01/01', 'NaN')

mask = nova_variavel['Date'] == '20201226'
nova_variavel.loc[mask, 'Date'] = pd.to_datetime(
    nova_variavel.loc[mask, 'Date'],
    format='%Y%m%d'
)

nova_variavel['Date'] = pd.to_datetime(nova_variavel['Date'], errors='coerce')
""" nova_variavel['Date'] = pd.to_datetime(nova_variavel['Date'], format='%Y/%m/%d', errors='coerce') """

nova_variavel = nova_variavel.dropna(subset=['Date'])

print("\n====Dataframe final====")
print(nova_variavel)
print("\n====Tipos de dados após a conversão====")
print(nova_variavel.dtypes)










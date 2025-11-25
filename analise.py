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












""" #Subconjunto de dados
df_sub = df[["ID", "Duration", "Date", "Pulse", "Maxpulse", "Calories"]]

#Tratamentos de tipos
df_sub["Duration"] = pd.to_numeric(df_sub["Duration"], errors='coerce')
df_sub["Pulse"] = pd.to_numeric(df_sub["Pulse"], errors='coerce')
df_sub["Maxpulse"] = pd.to_numeric(df_sub["Maxpulse"], errors='coerce')
df_sub["Calories"] = pd.to_numeric(df_sub["Calories"], errors='coerce')

#Num de registros
pd.set_option("display.max_rows", 10)


#Exibir as primeiras linhas
print(df_sub.head())


#Exibir informações
print(df_sub.info())
print(df_sub.describe())

# Trabalho prático: limpeza
df_sub["Date"] = pd.to_datetime(df_sub["Date"], errors='coerce', format='mixed')
df_sub = df_sub.drop_duplicates()
df_sub = df_sub.fillna({
    "Duration": df_sub["Duration"].mean(),
    "Pulse": df_sub["Pulse"].mean(),
    "Maxpulse": df_sub["Maxpulse"].mean(),
    "Calories": df_sub["Calories"].mean()
})

print(df_sub.corr())
import matplotlib.pyplot as plt

plt.scatter(df_sub["Duration"], df_sub["Calories"])
plt.xlabel("Duration (min)")
plt.ylabel("Calories")
plt.title("Relação entre Duração e Calorias")
plt.show()

for i in df_sub["ID"].unique():
    df_user = df_sub[df_sub["Id"] == i]
    df_user.plot(x="Date", y="Calories", kind="line", figsize=(8,4), title=f"Id {i} - Evolução das Calorias")

plt.scatter(df_sub["Pulse"], df_sub["Maxpulse"])
plt.xlabel("Pulse")
plt.ylabel("Maxpulse")
plt.title("Comparação entre Pulse e Maxpulse")
plt.show()


print(df.head())
 """

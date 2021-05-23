import pandas as pd
import numpy as np

# Carregando Dataframe
df_imob = pd.read_csv('../DataSets/melb_data.csv')

# Verificando como esta distrinuido os dados no DataFrame
print(df_imob.shape)

# Verificar as colunas
print(df_imob.columns)

# 1. Manuseio de datas

# Verificar qual tipo da coluna "Date"
print(df_imob.Date.dtypes)

# verificar como esta a Data antes da conversão

print('Verificando um mostra da data antes da conversão:{}'.format(df_imob.Date[:2]))

# Convertendo o tipo da coluna "Date"
df_imob['Date'] = pd.to_datetime(df_imob['Date'])

# verificar como esta a Data depois  da conversão

print('Verificando um mostra da data apos da conversão:{}'.format(df_imob.Date[:2]))

# 2. Alterando os tipos de dados

# verificando como o dados esta no formato float antes da conversão  para int

print(f'Verificando dados antes da conversão: {df_imob["Propertycount"][:2]}')

# Alterando o tipo da coluna de float para inteiro
df_imob['Propertycount'] = df_imob['Propertycount'].astype('int')

# Vializando o dados da coluna apos a conversão
print(f'Verificando dados apos da conversão: {df_imob["Propertycount"][:2]}')

#  #3. Substituindo valores

print(df_imob.head(3))

# Verificando os valores unicos da colunas 'Type' antes da conversão

print('Verificando dados antes da conversão : {}'.format(df_imob.Type.unique()))

# Executando o replace nos dados da colunas 'Type', referente a cada ocorrencia encontrada
df_imob.Type.replace({
    'h': 'casa',
    'u': 'unidade',
    't': 'casa_na_cidade'
}, inplace=True)

print('Verificando dados apos a conversão: {}'.format(df_imob.Type.unique()))

# Verificando os valores unicos da colunas 'Type' depois da conversão

# 4. ALterar o tipo de dados para melhor o consumo de recuso

print('Uso de memoria atual antes da conversção : {}'.format(df_imob.Type.memory_usage()))

df_imob['Type'] = df_imob['Type'].astype('category')

print('Uso de memoria atual apos a conversão: {}'.format(df_imob.Type.memory_usage()))

# 5. Extração de informações de datas

df_imob['Month'] = df_imob['Date'].dt.month

print('Verificar datas por dias da semanas: {}'.format(df_imob['Date'].dt.weekday[:5]))

print(df_imob['Month'][:5])

# 6. Extraindo informações do texto

# Visualizando os dados da coluna 'Address'
print(df_imob.Address[:5])

# Executando split da string contida nesta coluna , neste caso um endereço ,então realizando o split atraves do  ' '
# e pegando -1 que é referente ultima parte ,, por exemplo
print(df_imob['Address'].str.split(' ').str[-1][:5])

# Executando split da string contida nesta coluna , neste caso um endereço ,então realizando o split atraves do  ' '
# e pegando -2 que é referente segunda parte , por exemplo

print(df_imob['Address'].str.split(' ').str[-2][:5])

# 7. Padronizando os dados textuais

print(df_imob.Address.str.upper()[:5])

print(df_imob.Suburb[:5])
print(df_imob.Suburb.str.capitalize()[:5])
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

print(df_imob.Date[:2])

# Convertendo o tipo da coluna "Date"
df_imob['Date'] = pd.to_datetime(df_imob['Date'])

# verificar como esta a Data depois  da conversão

print(df_imob.Date[:2])

# 2. Alterando os tipos de dados

# verificando como o dados esta no formato float antes da conversão  para int

print(df_imob['Propertycount'][:2])

# Alterando o tipo da coluna de float para inteiro
df_imob['Propertycount'] = df_imob['Propertycount'].astype('int')

# Vializando o dados da coluna apos a conversão
print(df_imob['Propertycount'][:2])

#  #3. Substituindo valores

print(df_imob.head(3))

print(df_imob.Type.unique())

df_imob.Type.replace({
    'h': 'casa',
    'u': 'unidade',
    't': 'casa_na_cidade'
}, inplace=True)
print(df_imob.Type.unique())

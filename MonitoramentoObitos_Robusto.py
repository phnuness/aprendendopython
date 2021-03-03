import pandas as pd 
import numpy as np
import openpyxl
from os import system
from time import sleep

dados = "C://Users//pedro//Desktop//MONITORAMENTO_OBITOS.xlsx" #input(  "Informe o caminho da base com as informações de Status, Idade e Gênero: ")

obitos = pd.read_excel(dados, sheet_name=["2019", "2020", "2021"])

df_obitos = pd.concat([obitos['2019'], obitos['2020'], obitos['2021']])

df_obitos.insert(loc= 8, column='UNIDADE', value=1)

# Transformando coluna DT_OBITO para o tipo datetime

df_obitos['DT_OBITO'] = pd.to_datetime(df_obitos['DT_OBITO'])

# Criando a coluna ANO no dataframe com a identificação dos anos

df_obitos['ANO'] = df_obitos['DT_OBITO'].dt.year

# Total de óbitos geral

total_obitos = pd.DataFrame(df_obitos.groupby('ANO')['UNIDADE'].sum())

# Total de óbitos separados por movito

total_obitos_motivo = pd.DataFrame(df_obitos.groupby(['ANO', 'MOTIVO'])['UNIDADE'].sum())
total_obitos_motivo.columns.values[0] = 'TOTAL'

# Dataframe gerado a partir da base de óbitos filtrado por PLANO, UF e MOTIVO, que retorna a quantidade de óbitos por covid ou natural

obitos_plano_estado_motivo = pd.DataFrame(df_obitos.groupby(['ANO', 'PLANO', 'UF', 'MOTIVO']).sum()['UNIDADE']).unstack()['UNIDADE'].fillna(0)

# Dataframe filtrado por Plano, que retorna a quantidade de óbitos por covid ou natural

obitos_plano = pd.DataFrame(obitos_plano_estado_motivo.groupby(['ANO','PLANO'])['COVID19','NATURAL'].sum())

# Total de óbitos geral por Plano

total_obitos_plano = pd.DataFrame(obitos_plano.sum(axis=1))
total_obitos_plano['TOTAL'] = pd.DataFrame(obitos_plano.sum(axis=1))
total_obitos_plano = total_obitos_plano.iloc[:,[1]]

# Dataframe filtrado por Estado, que retorna a quantidade de óbitos por covid ou natural

obitos_uf = pd.DataFrame(obitos_plano_estado_motivo.groupby(['ANO','UF'])['COVID19','NATURAL'].sum())

# Total de óbitos geral por Estado

total_obitos_estado = pd.DataFrame(obitos_uf.sum(axis=1))
total_obitos_estado['TOTAL'] = pd.DataFrame(obitos_uf.sum(axis=1))
total_obitos_estado = total_obitos_estado.iloc[:,[1]]

# Dataframe gerado a partir da base de óbitos filtrado por PLANO, IDADE e MOTIVO, que retorna a quantidade de óbitos por covid ou natural para cada plano e para cada idade

df_obitos_idade = pd.DataFrame(df_obitos.groupby(['ANO','PLANO', 'IDADE', 'MOTIVO']).sum()['UNIDADE']).unstack()['UNIDADE'].fillna(0)

# Reset do index para realizar posteriormente os filtros por variações de idade

obitos_idade = df_obitos_idade.reset_index()

# Criando nova coluna com as variações de idade no novo dataframe


obitos_idade['INTERVALO_IDADES'] = [    '35 - 45' if i >= 35 and i <= 45 else
                                        '46 - 55' if i >= 46 and i <= 55 else
                                        '56 - 65' if i >= 56 and i <= 65 else
                                        '66 - 75' if i >= 66 and i <= 75 else
                                        '76 - 85' if i >= 76 and i <= 85 else
                                        '85 - 99' if i >= 86 and i <= 99 else
                                        '100+'
                                        for i in obitos_idade['IDADE']
                                        ]

# Dataframe gerado a partir do dataframe com intervalo de idades 'obitos_idades' filtrado por PLANO e INTERVALO_IDADES, que retorna a quantidade de óbitos por covid ou natural para cada plano dentro das variações de idade

obitos_plano_intervalo_idade = pd.DataFrame(obitos_idade.groupby(['ANO', 'PLANO', 'INTERVALO_IDADES'])['COVID19', 'NATURAL'].sum())

# Dataframe que retorna a quantidade de óbitos por covida e natural por intervalo de idade

obitos_intervalo_idade = pd.DataFrame(obitos_idade.groupby(['ANO', 'INTERVALO_IDADES'])['COVID19', 'NATURAL'].sum())

# Dataframe que retorna a quantidade de óbitos por covid no intervalo de idades

obitos_intervalo_idade_covid = pd.DataFrame(obitos_intervalo_idade.groupby(['ANO','INTERVALO_IDADES']).sum()['COVID19'])

# Dataframe que retorna a quantidade de óbitos naturais no intervalo de idades

obitos_intervalo_idade_natural = pd.DataFrame(obitos_intervalo_idade.groupby(['ANO', 'INTERVALO_IDADES']).sum()['NATURAL'])

# Dataframe que retorna a quantidade total de óbitos (covid + natural) no intervalo de idades

total_obitos_intervalo_idades = pd.DataFrame(obitos_intervalo_idade_natural.sum(axis=1))
total_obitos_intervalo_idades['TOTAL'] = pd.DataFrame(obitos_intervalo_idade_natural.sum(axis=1))
total_obitos_intervalo_idades = total_obitos_intervalo_idades.iloc[:,[1]]

# Dataframe gerado a partir da base de óbitos filtrado por MES_OBITO, que retorna a quantidade de óbitos para cada mes

total_obitos_mes = pd.DataFrame(df_obitos.groupby(['ANO','MES_OBITO'])['UNIDADE'].sum())
total_obitos_mes.rename(columns={'UNIDADE':'TOTAL'}, inplace=True)

# Dataframe gerado a partir da base de óbitos filtrado por PLANO, MES_OBITO e MOTIVO, que retorna a quantidade de óbitos por covid ou natural para cada plano e mes

obitos_plano_mes_motivo = pd.DataFrame(df_obitos.groupby(['ANO', 'PLANO', 'MES_OBITO', 'MOTIVO']).sum()['UNIDADE']).unstack()['UNIDADE'].fillna(0)

# Dataframe gerado a partir do dataframe filtrato por PLANO, MES_OBITO e MOTIVO, que retorna a quantidade de óbitos por covid ou natural para cada mes

obitos_mes_motivo = pd.DataFrame(obitos_plano_mes_motivo.groupby(['ANO', 'MES_OBITO'])['COVID19','NATURAL'].sum())

# Resetando o index

df_total_obitos_mes = total_obitos_mes.reset_index()

# Dataframe com total de óbitos acumulados de 2019, 2020 e 2021


df_total_obitos_mes_ano = df_total_obitos_mes.groupby(['MES_OBITO', 'ANO']).sum().unstack()['TOTAL'].fillna(0)
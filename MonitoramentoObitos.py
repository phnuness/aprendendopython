import pandas as pd 
import numpy as np
import openpyxl

dados = "C://Users//pedro//Desktop//MONITORAMENTO_OBITOS.xlsx" #input(  "Informe o caminho da base com as informações de Status, Idade e Gênero: ")

obitos_2019 = pd.read_excel(dados, sheet_name="2019")
obitos_2020 = pd.read_excel(dados, sheet_name="2020")
obitos_2021 = pd.read_excel(dados, sheet_name="2021")

obitos_2019.insert(loc= 8, column='UNIDADE', value=1)
obitos_2020.insert(loc= 8, column='UNIDADE', value=1)
obitos_2021.insert(loc= 8, column='UNIDADE', value=1)

# obitos_2020['COVID19'].value_counts() - Para contar os valores, ex: quantidade para sim e não

# Total de óbitos geral

total_obitos_2019 = obitos_2019['UNIDADE'].sum()
total_obitos_2020 = obitos_2020['UNIDADE'].sum()
total_obitos_2021 = obitos_2021['UNIDADE'].sum()

# Total de óbitos separados por movito

total_obitos_motivo_2019 = pd.DataFrame(obitos_2019.groupby('MOTIVO')['UNIDADE'].sum())
total_obitos_motivo_2020 = pd.DataFrame(obitos_2020.groupby('MOTIVO')['UNIDADE'].sum())
total_obitos_motivo_2021 = pd.DataFrame(obitos_2021.groupby('MOTIVO')['UNIDADE'].sum())

# Dataframe gerado a partir da base de óbitos filtrado por PLANO, UF e MOTIVO, que retorna a quantidade de óbitos por covid ou natural

#obitos_plano_estado_motivo_2019 = pd.DataFrame(obitos_2019.groupby(['PLANO', 'UF', 'MOTIVO']).sum()['UNIDADE']).unstack()['UNIDADE'].fillna(0)
obitos_plano_estado_motivo_2020 = pd.DataFrame(obitos_2020.groupby(['PLANO', 'UF', 'MOTIVO']).sum()['UNIDADE']).unstack()['UNIDADE'].fillna(0)
obitos_plano_estado_motivo_2021 = pd.DataFrame(obitos_2021.groupby(['PLANO', 'UF', 'MOTIVO']).sum()['UNIDADE']).unstack()['UNIDADE'].fillna(0)

# Dataframe filtrado por Plano, que retorna a quantidade de óbitos por covid ou natural

#obitos_plano_2019 = pd.DataFrame(obitos_plano_estado_motivo_2019.groupby(['PLANO'])['COVID19','NATURAL'].sum())
obitos_plano_2020 = pd.DataFrame(obitos_plano_estado_motivo_2020.groupby(['PLANO'])['COVID19','NATURAL'].sum())
#obitos_plano_2021 = pd.DataFrame(obitos_plano_estado_motivo_2021.groupby(['PLANO'])['COVID19','NATURAL'].sum())

# Total de óbitos geral por Plano

#total_obitos_plano_2019 = pd.DataFrame(obitos_plano_2019['COVID19'] + obitos_plano_2019['NATURAL'])
total_obitos_plano_2020 = pd.DataFrame(obitos_plano_2020['COVID19'] + obitos_plano_2020['NATURAL'])
#total_obitos_plano_2021 = pd.DataFrame(obitos_plano_2021['COVID19'] + obitos_plano_2021['NATURAL'])

# Dataframe filtrado por Estado, que retorna a quantidade de óbitos por covid ou natural

#obitos_uf_2019 = pd.DataFrame(obitos_plano_estado_motivo_2019.groupby(['UF'])['COVID19','NATURAL'].sum())
obitos_uf_2020 = pd.DataFrame(obitos_plano_estado_motivo_2020.groupby(['UF'])['COVID19','NATURAL'].sum())
#obitos_uf_2021 = pd.DataFrame(obitos_plano_estado_motivo_2021.groupby(['UF'])['COVID19','NATURAL'].sum())

# Total de óbitos geral por Estado

#total_obitos_estado_2019 = pd.DataFrame(obitos_uf_2019['COVID19'] + obitos_uf_2019['NATURAL'])
total_obitos_estado_2020 = pd.DataFrame(obitos_uf_2020['COVID19'] + obitos_uf_2020['NATURAL'])
#total_obitos_estado_2021 = pd.DataFrame(obitos_uf_2021['COVID19'] + obitos_uf_2021['NATURAL'])

# Dataframe gerado a partir da base de óbitos filtrado por PLANO, IDADE e MOTIVO, que retorna a quantidade de óbitos por covid ou natural para cada plano e para cada idade

#df_obitos_idade_2019 = pd.DataFrame(obitos_2019.groupby(['PLANO', 'IDADE', 'MOTIVO']).sum()['UNIDADE']).unstack()['UNIDADE'].fillna(0)
df_obitos_idade_2020 = pd.DataFrame(obitos_2020.groupby(['PLANO', 'IDADE', 'MOTIVO']).sum()['UNIDADE']).unstack()['UNIDADE'].fillna(0)
#df_obitos_idade_2021 = pd.DataFrame(obitos_2021.groupby(['PLANO', 'IDADE', 'MOTIVO']).sum()['UNIDADE']).unstack()['UNIDADE'].fillna(0)

# Reset do index para realizar posteriormente os filtros por variações de idade

#obitos_idade_2019 = df_obitos_idade_2019.reset_index()
obitos_idade_2020 = df_obitos_idade_2020.reset_index()
#obitos_idade_2021 = df_obitos_idade_2021.reset_index()

# Criando nova coluna com as variações de idade no novo dataframe
'''
obitos_idade_2019['INTERVALO_IDADES'] = [    '35 - 45' if i >= 35 and i <= 45 else
                                        '46 - 55' if i >= 46 and i <= 55 else
                                        '56 - 65' if i >= 56 and i <= 65 else
                                        '66 - 75' if i >= 66 and i <= 75 else
                                        '76 - 85' if i >= 76 and i <= 85 else
                                        '85 - 99' if i >= 86 and i <= 99 else
                                        '100+'
                                        for i in obitos_idade_2019['IDADE']
                                        ]
'''
obitos_idade_2020['INTERVALO_IDADES'] = [    '35 - 45' if i >= 35 and i <= 45 else
                                        '46 - 55' if i >= 46 and i <= 55 else
                                        '56 - 65' if i >= 56 and i <= 65 else
                                        '66 - 75' if i >= 66 and i <= 75 else
                                        '76 - 85' if i >= 76 and i <= 85 else
                                        '85 - 99' if i >= 86 and i <= 99 else
                                        '100+'
                                        for i in obitos_idade_2020['IDADE']
                                        ]
'''
obitos_idade_2021['INTERVALO_IDADES'] = [    '35 - 45' if i >= 35 and i <= 45 else
                                        '46 - 55' if i >= 46 and i <= 55 else
                                        '56 - 65' if i >= 56 and i <= 65 else
                                        '66 - 75' if i >= 66 and i <= 75 else
                                        '76 - 85' if i >= 76 and i <= 85 else
                                        '85 - 99' if i >= 86 and i <= 99 else
                                        '100+'
                                        for i in obitos_idade_2021['IDADE']
                                        ]
'''
# Dataframe gerado a partir do dataframe com intervalo de idades 'obitos_idades' filtrado por PLANO e INTERVALO_IDADES, que retorna a quantidade de óbitos por covid ou natural para cada plano dentro das variações de idade

#obitos_intervalo_idade_2019 = pd.DataFrame(obitos_idade_2019.groupby(['PLANO', 'INTERVALO_IDADES'])['COVID19', 'NATURAL'].sum())
obitos_intervalo_idade_2020 = pd.DataFrame(obitos_idade_2020.groupby(['PLANO', 'INTERVALO_IDADES'])['COVID19', 'NATURAL'].sum())
#obitos_intervalo_idade_2021 = pd.DataFrame(obitos_idade_2021.groupby(['PLANO', 'INTERVALO_IDADES'])['COVID19', 'NATURAL'].sum())

# Dataframe que retorna a quantidade de óbitos por covid no intervalo de idades

#obitos_intervalo_idade_covid_2019 = pd.DataFrame(obitos_intervalo_idade_2019.groupby(['INTERVALO_IDADES']).sum()['COVID19']) 
obitos_intervalo_idade_covid_2020 = pd.DataFrame(obitos_intervalo_idade_2020.groupby(['INTERVALO_IDADES']).sum()['COVID19'])
#obitos_intervalo_idade_covid_2021 = pd.DataFrame(obitos_intervalo_idade_2021.groupby(['INTERVALO_IDADES']).sum()['COVID19'])

# Dataframe que retorna a quantidade de óbitos naturais no intervalo de idades

#obitos_intervalo_idade_natural_2019 = pd.DataFrame(obitos_intervalo_idade_2019.groupby(['INTERVALO_IDADES']).sum()['NATURAL'])
obitos_intervalo_idade_natural_2020 = pd.DataFrame(obitos_intervalo_idade_2020.groupby(['INTERVALO_IDADES']).sum()['NATURAL'])
#obitos_intervalo_idade_natural_2021 = pd.DataFrame(obitos_intervalo_idade_2021.groupby(['INTERVALO_IDADES']).sum()['NATURAL'])

# Dataframe que retorna a quantidade total de óbitos (covid + natural) no intervalo de idades

#total_obitos_intervalo_idades_2019 = pd.DataFrame(obitos_intervalo_idade_natural_2019['NATURAL'] + obitos_intervalo_idade_covid_2019 ['COVID19'])
total_obitos_intervalo_idades_2020 = pd.DataFrame(obitos_intervalo_idade_natural_2020['NATURAL'] + obitos_intervalo_idade_covid_2020 ['COVID19'])
#total_obitos_intervalo_idades_2021 = pd.DataFrame(obitos_intervalo_idade_natural_2021['NATURAL'] + obitos_intervalo_idade_covid_2019 ['COVID19'])

# Dataframe gerado a partir da base de óbitos filtrado por MES_OBITO, que retorna a quantidade de óbitos para cada mes

total_obitos_mes_2019 = pd.DataFrame(obitos_2019.groupby('MES_OBITO')['UNIDADE'].sum())
total_obitos_mes_2020 = pd.DataFrame(obitos_2020.groupby('MES_OBITO')['UNIDADE'].sum())
total_obitos_mes_2021 = pd.DataFrame(obitos_2021.groupby('MES_OBITO')['UNIDADE'].sum())

# Dataframe gerado a partir da base de óbitos filtrado por PLANO, MES_OBITO e MOTIVO, que retorna a quantidade de óbitos por covid ou natural para cada plano e mes

#obitos_plano_mes_motivo_2019 = pd.DataFrame(obitos_2019.groupby(['PLANO', 'MES_OBITO', 'MOTIVO']).sum()['UNIDADE']).unstack()['UNIDADE'].fillna(0)
obitos_plano_mes_motivo_2020 = pd.DataFrame(obitos_2020.groupby(['PLANO', 'MES_OBITO', 'MOTIVO']).sum()['UNIDADE']).unstack()['UNIDADE'].fillna(0)
#obitos_plano_mes_motivo_2021 = pd.DataFrame(obitos_2021.groupby(['PLANO', 'MES_OBITO', 'MOTIVO']).sum()['UNIDADE']).unstack()['UNIDADE'].fillna(0)

# Dataframe gerado a partir do dataframe filtrato por PLANO, MES_OBITO e MOTIVO, que retorna a quantidade de óbitos por covid ou natural para cada mes

#obitos_mes_motivo_2019 = pd.DataFrame(obitos_plano_mes_motivo_2019.groupby(['MES_OBITO'])['COVID19','NATURAL'].sum())
obitos_mes_motivo_2020 = pd.DataFrame(obitos_plano_mes_motivo_2020.groupby(['MES_OBITO'])['COVID19','NATURAL'].sum())
#obitos_mes_motivo_2021 = pd.DataFrame(obitos_plano_mes_motivo_2021.groupby(['MES_OBITO'])['COVID19','NATURAL'].sum())

# Resetando o index

total_obitos_mes_2019 = total_obitos_mes_2019.reset_index()
total_obitos_mes_2020 = total_obitos_mes_2020.reset_index()
total_obitos_mes_2021 = total_obitos_mes_2021.reset_index()

# Dataframe com total de óbitos acumulados de 2019, 2020 e 2021

total_obitos_mes_2019_2020_2021 = pd.concat([total_obitos_mes_2019, total_obitos_mes_2020, total_obitos_mes_2021], axis=1).fillna('')
total_obitos_mes_2019_2020_2021.columns.values[1] = '2019'
total_obitos_mes_2019_2020_2021.columns.values[3] = '2020'
total_obitos_mes_2019_2020_2021.columns.values[5] = '2021'
total_obitos_mes_2019_2020_2021 = total_obitos_mes_2019_2020_2021.iloc[:,[0,1,3,5]]

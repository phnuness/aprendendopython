import pandas as pd 
import numpy as np
import openpyxl

dados = "C://Users//pedro//Desktop//MONITORAMENTO_OBITOS.xlsx" #input(  "Informe o caminho da base com as informações de Status, Idade e Gênero: ")

obitos_2019 = pd.read_excel(dados, sheet_name="2019")
obitos_2020 = pd.read_excel(dados, sheet_name="2020")
obitos_2021 = pd.read_excel(dados, sheet_name="2021")

obitos_2019.insert(loc= 6, column='UNIDADE', value=1)
obitos_2020.insert(loc= 8, column='UNIDADE', value=1)
obitos_2021.insert(loc= 8, column='UNIDADE', value=1)

# obitos_2020['COVID19'].value_counts() - Para contar os valores, ex: quantidade para sim e não

# Dataframe gerado a partir da base de óbitos filtrado por PLANO, UF e MOTIVO, que retorna a quantidade de óbitos por covid ou natural

obitos_plano_estado_motivo_2020 = pd.DataFrame(obitos_2020.groupby(['PLANO', 'UF', 'MOTIVO']).sum()['UNIDADE']).unstack()['UNIDADE'].fillna(0)

# Dataframe filtrado por Plano, que retorna a quantidade de óbitos por covid ou natural

obitos_plano = pd.DataFrame(obitos_plano_estado_motivo_2020.groupby(['PLANO'])['COVID19','NATURAL'].sum())

# Total de óbitos separados por movito

total_obitos_motivo = pd.DataFrame(obitos_2020.groupby('MOTIVO')['UNIDADE'].sum())

# Total de óbitos geral

total_obitos = obitos_2020['UNIDADE'].sum()

# Total de óbitos geral por Plano

total_obitos_plano = pd.DataFrame(obitos_plano['COVID19'] + obitos_plano['NATURAL'])

# Dataframe filtrado por Estado, que retorna a quantidade de óbitos por covid ou natural

obitos_uf = pd.DataFrame(obitos_plano_estado_motivo_2020.groupby(['UF'])['COVID19','NATURAL'].sum())

# Total de óbitos geral por Estado

total_obitos_estado = pd.DataFrame(obitos_uf['COVID19'] + obitos_uf['NATURAL'])

# Dataframe gerado a partir da base de óbitos filtrado por PLANO, IDADE e MOTIVO, que retorna a quantidade de óbitos por covid ou natural para cada plano e para cada idade

obitos_idade = pd.DataFrame(obitos_2020.groupby(['PLANO', 'IDADE', 'MOTIVO']).sum()['UNIDADE']).unstack()['UNIDADE'].fillna(0)

# Reset do index para realizar posteriormente os filtros por variações de idade

obitos_idade = obitos_idade.reset_index()

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

obitos_intervalo_idade = pd.DataFrame(obitos_idade.groupby(['PLANO', 'INTERVALO_IDADES'])['COVID19', 'NATURAL'].sum())

# Dataframe que retorna a quantidade de óbitos por covid no intervalo de idades
 
obitos_intervalo_idade_covid = pd.DataFrame(obitos_intervalo_idade.groupby(['INTERVALO_IDADES']).sum()['COVID19'])

# Dataframe que retorna a quantidade de óbitos naturais no intervalo de idades

obitos_intervalo_idade_natural = pd.DataFrame(obitos_intervalo_idade.groupby(['INTERVALO_IDADES']).sum()['NATURAL'])

# Dataframe que retorna a quantidade total de óbitos (covid + natural) no intervalo de idades

total_obitos_intervalo_idades = pd.DataFrame(obitos_intervalo_idade_natural['NATURAL'] + obitos_intervalo_idade_covid ['COVID19'])
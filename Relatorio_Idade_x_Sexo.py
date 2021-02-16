import pandas as pd 
import openpyxl

dados = input(  "Informe o caminho da base com as informações de Status, Idade e Gênero: ")
#'C:\\Users\\pedro\\Desktop\\OBITOS.xlsx'
aba = input("Informe o nome da aba a ser utilizada na planilha inserida anteriormente: ")
plano = input("Informe o caminho que deseja salvar o arquivo gerado com a extensão xlsx: ")

def obter_dados (caminho):
    dataframe = pd.read_excel(caminho, sheet_name=aba)
    return dataframe

df = obter_dados(dados)

df.insert(loc= 11, column='UNIDADE', value=1)

genero = pd.DataFrame(df.groupby(['PLANO', 'IDADE', 'GENERO']).sum()['UNIDADE']).unstack()['UNIDADE'].fillna(0)

genero = genero.reset_index()

genero['INTERVALO'] = [ 'Até 24 anos' if i <= 24 else
                        '24 a 35' if i >23 and i <36 else
                        '36 a 55' if i >35 and i <56 else
                        '56 a 76'
                        for i in genero['IDADE']]

intervalo = pd.DataFrame(genero.groupby(['INTERVALO', 'PLANO'])['F', 'M'].sum())

intervalo.to_excel(plano)

print(intervalo)
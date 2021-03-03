from lib.interface import *

while True:
    # Menu principal do Sistema
    cabecalho('Menu Principal')
    formatar_menu([
        'Total de óbitos anual'
        'Total de óbitos anual por motivo'
        'Total de óbitos por plano'
        'Total de óbitos por plano e motivo'
        'Total de óbitos por estado'
        'Total de óbitos por estado e motivo'
        'Total de óbitos por intervalo de idades'
        'Total de óbitos por intervalo de idades e motivo'
        'Total de óbitos por plano com intervalo de idades e motivo'
        'Total de óbitos por mês'
        'Total de óbitos por mês e motivo'
        'Total de óbitos por anos e meses'

    ])
    selecao = opcao_menu_principal()
def linha(tam=40):
    """Gerar linha
    Args:
        tam (int, optional): tamanho da linha. Defaults to 40.
    Returns:
        str: linha com tamanho informado
    """
    tam = 50
    return '=' * tam

def cabecalho(msg):
    """Cabecalho formatado
    Args:
        msg (str): Texto centralizado
    """
    print(linha())
    print(msg.center(50))
    print(linha())

def leia_int(msg):
    """Ler numeros inteiros
    Args:
        msg (str): Mensagem mostrada ao usuario
    Returns:
        int: valor inteiro
    """
    while True:
        try:
            n = int(input(msg))
        except:
            print('ERRO! Por favor digite um valor inteiro válido.')
            continue
        else:
            return n

def formatar_menu(lista):
    """Criar menu formatado sobre uma lista
    Args:
        lista (str): lista com as opcoes do menu
    """
    for pos, item in enumerate(lista):
        print(f'[{pos+1}] - {item}')
    print(linha())

def opcao_menu_principal():
    """Ler opcao informada pelo usuário
    Returns:
        int: Opcao informada
    """
    op = leia_int('Sua opção: ')
    return op

def opcao_cadastro():
    """Ler opcao informada pelo usuário
    Returns:
        int : Opcao informada convertida para inteiro
    """
    opcao = str(input('Opção(ões) de cadastro: ')).split(',')
    return opcao
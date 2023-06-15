def aumentar(preco, taxa, format=False):
    '''

    :param preco:
    :param taxa:
    :param format:
    :return:
    '''
    res = preco + (preco * taxa/100)
    return res if format is False else moeda(res)


def diminuir(preco, taxa, format=False):
    res = preco - (preco * taxa / 100)
    return res if format is False else moeda(res)


def dobro(preco, format=False):
    res = preco * 2
    return res if format is False else moeda(res)


def metade(preco, format=False):
    res = preco / 2
    return res if format is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(p=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DE VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado : \t\t{moeda(p)}')
    print(f'Metade do preço: \t\t{metade(p, True)}')
    print(f'Dobro do preço: \t\t{dobro(p, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(p, taxaa, True)}')
    print(f'Com {taxar}% de redução: \t\t{diminuir(p, taxar, True)}')


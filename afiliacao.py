'''
- Coleta o produto do proprietário
- Coleta a comissão dos afiliados
- Coleta as vendas de cada afiliado
- Aumenta a comissão do top afiliado
'''

def produto():
    '''
    0 - tipo do produto
    1 - preço unitário do produto
    2 - comissão dos afiliados (em %)
    '''
    produtos_info = []
    produto = input('\nDigite o tipo do seu produto: ')
    produtos_info.append(produto)
    preco = float(input('Digite o preço unitário: R$'))
    produtos_info.append(preco)
    comissao = float(input('Digite a comissão dos seus afiliados (em %): '))
    produtos_info.append(comissao)
    return produtos_info

def afiliados():
    '''
    0 - nome afiliado
    1 - vendas do afiliado
    '''
    afiliados_info = []
    nome = input('\nDigite o nome do afiliado: ')
    afiliados_info.append(nome)
    vendas = float(input(f'Digite quantas vendas {nome} fez: '))
    afiliados_info.append(vendas)
    return afiliados_info

def comissao_afiliado(valor_produto, taxa_comissao, vendas):
    taxa_comissao /= 100
    valor_comissao = valor_produto * vendas * taxa_comissao
    return valor_comissao

def infos_afiliados(valor_comissao, afiliado):
    infos = (afiliado[0], afiliado[1], valor_comissao)
    return infos

def print_dash_produto(produto_info):
    print('\n-----------------------------------------------------------------------------------------------------------------------------------')
    print('\nDASHBOARD DO PRODUTO')
    print('\nPRODUTO')
    print(f'Tipo: {produto_info[0]}')
    print(f'Preço Unitário: R${produto_info[1]:.2f}')
    print(f'Taxa de Comissão dos afiliados: {produto_info[2]:.1f}%')

def print_dash_afiliados(lista_afiliados, produto_info):
    i = 1
    print('\nAFILIADOS')
    for a, b, c in lista_afiliados:
        valor_vendas = produto_info[1] * (b)
        print(f'Afiliado {i}: {a} - Produtos vendidos: {b:.0f} - Valor em vendas: R${valor_vendas:.2f} - Valor em comissão: R$ {c:.2f}')
        i+=1
    print('\n-----------------------------------------------------------------------------------------------------------------------------------')

def main():
    print('*- Seja bem-vindo ao programa de afiliação! -*')
    produto_info = produto()
    lista_afiliados = []
    valor_produto = produto_info[1]
    taxa_comissao = produto_info[2]
    while True:
        afiliado = afiliados()
        valor_comissao = comissao_afiliado(valor_produto, taxa_comissao, afiliado[1])
        infos = infos_afiliados(valor_comissao, afiliado)
        lista_afiliados.append(infos)
        continuar = input('\nDeseja adicionar mais um afiliado? (Sim ou não): ')
        if continuar.lower() == 'não' or continuar.lower() == 'nao':
            break
        elif continuar.lower() == 'sim':
            continue
    
    print_dash_produto(produto_info)
    print_dash_afiliados(lista_afiliados, produto_info)

main()
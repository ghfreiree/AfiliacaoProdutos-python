'''
- Coleta as informações do produto do proprietário
- Coleta as informações dos afiliados
- Calcula a comissão de cada afiliado
- Exibe um dashboard com as informações do produto e dos afiliados
- Permite adicionar informações de outro produto
'''

def produto():
    '''
    Retorna lista com informações do produto:
    [0] - tipo do produto
    [1] - preço unitário do produto
    [2] - comissão dos afiliados (em %)
    '''
    produtos_info = []
    produto = input('\nDigite o tipo do seu produto: ')
    produtos_info.append(produto)
    preco = float(input('Digite o preço unitário: R$'))
    produtos_info.append(preco)
    comissao = float(input('Digite a comissão dos seus afiliados (em %): '))
    produtos_info.append(comissao)
    return produtos_info

def cadastro_afiliados():
    '''
    Retorna lista com informações do afiliado:
    [0] - nome afiliado
    [1] - vendas do afiliado
    '''
    afiliados_info = []
    nome = input('\nDigite o nome do afiliado: ')
    afiliados_info.append(nome)
    while True:
        vendas = float(input(f'Digite quantas vendas {nome} fez: '))
        if vendas < 0:
            print('Número de vendas não pode ser negativo. Tente novamente.')
        else:
            break
    afiliados_info.append(vendas)
    return afiliados_info

def calc_comissao(valor_produto, taxa_comissao, vendas):
    taxa_comissao /= 100
    valor_comissao = valor_produto * vendas * taxa_comissao
    return valor_comissao

def infos_afiliados(valor_comissao, afiliado):
    infos = (afiliado[0], afiliado[1], valor_comissao)
    return infos

def print_dash_produto(produto_info):
    print('\n-----------------------------------------------------------------------------------------------------------------------------------')
    print('\nDASHBOARD')
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
    while True:

        # Pega as informações do produto
        produto_info = produto()
        lista_afiliados = []
        valor_produto = produto_info[1]
        taxa_comissao = produto_info[2]

        # Operação do sistema
        while True:
            afiliados = cadastro_afiliados()
            valor_comissao = calc_comissao(valor_produto, taxa_comissao, afiliados[1])
            infos = infos_afiliados(valor_comissao, afiliados)
            lista_afiliados.append(infos)
            while True:
                continuar = input('\nDeseja adicionar mais um afiliado? (Sim ou não): ')
                if continuar.lower() == 'não' or continuar.lower() == 'nao':
                    break
                elif continuar.lower() == 'sim':
                    break
                else:
                    print('Opção inválida. Digite "Sim" ou "Não".')
            if continuar.lower() == 'não' or continuar.lower() == 'nao':
                break
                
        print_dash_produto(produto_info)
        print_dash_afiliados(lista_afiliados, produto_info)

        # Opção de adicionar mais um produto
        while True:
            adicionar = input('\nDeseja cadastrar informações de outro produto? (Sim ou não): ')
            if adicionar.lower() == 'não' or adicionar.lower() == 'nao':
                print('\nObrigado por utilizar o programa de afiliação! Até mais!')
                break
            elif adicionar.lower() == 'sim':
                break
            else:
                print('Opção inválida. Digite "Sim" ou "Não".')
        if adicionar.lower() == 'não' or adicionar.lower() == 'nao':
            break

main()
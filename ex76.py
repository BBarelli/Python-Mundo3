'''
Exercício Python 076:
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
print('-'*40)
print('LISTAGEM DE PRODUTOS')
print('-'*40)

listagem = ('lápis', 5.0,
            'caderno', 20.0,
            'estojo', 15.0,
            'borracha', 10.0,
            'mochila', 30.0,
            'apontador', 8.0)
for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')

print(f'{'Fim do programa'}')
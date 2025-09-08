'''
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

valornum = []
n = 0
while True:
    n = int(input('Digite um valor: '))
    if n not in valornum:
        valornum.append(n)
        print('Valor adicionado!')
    else:
        print('Valor duplicado')

    escolha = str(input('Você deseja continuar [S/N]: ')).strip().upper()

    if escolha == 'N':
        break

print('=-'*20)

valornum.sort()
print(f'Você digitou {valornum}')

print('Fim do programa')
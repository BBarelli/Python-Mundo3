'''
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''

num = []
lista_par = []
lista_impar = []

while True:
    num.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar a digitação [S/N]: ')).strip().upper()

    if num[-1] % 2 == 0:
        lista_par.append(num[-1]) # num[-1] pega o último número digitado
    else:
        lista_impar.append(num[-1]) # num[-1] pega o último número digitado
    
    if r == 'N':
        break

print(f'Lista digitada: {num}')
print(f'Número Pares: {lista_par}')
print(f'Número Impares: {lista_impar}')


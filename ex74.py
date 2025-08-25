'''
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

# Gerar um número inteiro aleatório entre 1 e 10, inclusive
numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)

#Por padrão, o print() no Python termina com uma quebra de linha (\n).
O parâmetro (end='') muda esse comportamento.
end='\n' → padrão (pula linha no final).
end='' → nada é colocado no final.
end=' ' → coloca um espaço em vez de quebra de linha.

'''
from random import randint

num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram: ')

for n in num:
    print(f'{n}', end=',')
print(f'\nO maior número sorteado foi: {max(num)}') #O método 'max' seleciona o maior número em uma sequência
print(f'O menor número sorteado foi: {min(num)}')#Ou o minimo
print('Fim do programa')



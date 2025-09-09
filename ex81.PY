'''
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.   
A) Quantos números foram digitados
B) A lista de valores, ordenada de forma decrescente.  
C) Se o valor 5 foi digitado e está ou não na lista.
'''

num = []
digitado = 0
while True:
    num.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar [S/N]: ')).strip().upper()

    if r == 'S':
        digitado += 1

    if r not in 'SN':
        print('Não entendi sua resposta.')
        r = str(input('Deseja continuar [S/N]: ')).strip().upper()       

    if r == 'N':
        break

print(f'Tivemos um total de {len(num)} número digitados') #A

num.sort(reverse=True) #B
print(num)

if 5 in num: #C
    print('O número 5 foi digitado na lista')
else: 
    print('O número 5 não foi digitado na lista')

print('Fim do programa')


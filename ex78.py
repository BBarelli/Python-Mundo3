'''
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
#Breno Barelli
def exercicio78():
    valores = []
    for v in range(0, 5): #(i: índice, v: valor)
        valores.append(int(input(f'Digite um valor para a posição {v}: ')))

    print('=-'*15)
    print(f'Você digitou os valores {valores}\n')

    maior = max(valores)
    menor = min(valores)

    for i, v in enumerate(valores):
        if v == maior:
            print(f'O maior valor digitado foi: {maior} e está na posição {i}')
    
    for i, v in enumerate(valores):
        if v == menor:
            print(f'O maior valor digitado foi: {menor} e está na posição {i}')

    print('Fim do programa')

#Guanabara
def Exercicio79():
    listanum = []
    maior = 0
    menor = 0
    for v in range (0,5):
        listanum.append(int(input(f'Digite um valor para a posição {v}: ')))
        if v == 0:
            maior = menor = listanum[v]
        else:
            if listanum[v] > maior:
                maior = listanum[v]
            if listanum[v] < menor:
                menor = listanum[v]

    print(f'\nVocê digitou os valores {listanum}\n')

    for i, v in enumerate(listanum):
        if v == maior:
            print(f'O maior valor digitado foi: {maior} e está na posição {i}')

    for i, v in enumerate(listanum):
        if v == menor:
            print(f'O menor valor digitado foi: {menor} e está na posição {i}')
    print('Fim do programa')


exercicio78()
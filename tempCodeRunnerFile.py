def Exercicio79():
    listanum = []
    maior = 0
    menor = 0
    for v in range (0,5):
        listanum.append(int(input(f'Digite um valor para a posição {v}: ')))
        if listanum == 0:
            maior = menor = listanum[v]
        else:
            if listanum[v] > 0:
            maior = listanum[v]
            if listanum[v] < 0:
            menor = listanum[v]
    print(f'Você digitou os valores {listanum}\n')

Exercicio79()
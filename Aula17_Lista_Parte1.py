'''
VARIÁVEIS COMPOSTAS (LISTA)
"AS LISTAS NÃO SÃO IMUTÁVEIS" ELAS PODEM MUDAR!

EXEMPLOS DE LISTA:
*váriavel:
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

Mas...se eu quiser mudar um elemento da lista?

lanche[4] = 'sorvete'

*pro sistema:
lanche = 0, 1, 2, 3, 4

Pra ADICIONAR um elemento na lista:
lanche.append('sorvete') -> Adiciona o elemento no final da lista
lanche.insert(0, 'sorvete') -> Adiciona o elemento na posição desejada

Pra REMOVER um elemento da lista:
lanche.remove('suco') -> Não remove o indice e sim o valor desejado
lanche.pop() -> Remove o último elemento da lista
lanche.pop(1) -> Remove o elemento da posição desejada
del lanche[3] -> Deleta o elemento da posição desejada
lanche.clear() -> Limpa toda a lista

Podemos criar usando o comando (if) para verificar se o elemento está na lista antes de remover
if 'pizza' in lanche:
    lanche.remove('pizza')
else:
    print('Não achei o elemento')

Podemos usar o comando (len) para saber o tamanho da lista
len(lanche)
print(f'Eu vou comer {len(lanche)} tipos de comida')

Podemos usar o comando (sorted) para colocar a lista em ordem alfabética
print(sorted(lanche)) -> Mostra em ordem alfabética, mas não altera a lista 

Podemos usar o comando (range) para criar uma lista numérica
valores = list(range(4, 11)) -> Cria uma lista do 4 ao 10
print(valores)

valores = list(range(0, 11, 2)) -> Cria uma lista do 0 ao 10 de 2 em 2
print(valores)

Podemos usar o comando (enumerate) para mostrar o índice e o valor da lista
for c, v in enumerate(lanche):
    print(f'Eu vou comer {v} na posição {c}')

    
Podemos usar o comando (split) para separar os elementos da lista
a = 'Breno Silva Pereira'
print(a.split()) -> Separa os elementos da string e cria uma lista  

Organizar a ordem númerica da lista
valores.sort() -> Coloca em ordem crescente
valores.sort(reverse=True) -> Coloca em ordem decrescente

Podemos usar o comando (copy) para copiar uma lista para outra
b = a[:] -> Cópia da lista A para a lista B
b = a.copy() -> Cópia da lista A para a lista B

**Posso começar uma lista vazia, das seguintes formas:
valores = []
valores = list()
'''

# PRÁTICA
num = [2, 5, 9, 1]
num[2] = 3 #Muda o valor do índice 2
num.append(7) #Adiciona o valor 7 no final da lista
num.sort() #Coloca em ordem crescente
num.sort(reverse=True) #Coloca em ordem decrescente
num.insert(2, 0) #Adiciona o valor '0' na posição 2
num.remove(2) #Remove o valor 2 da lista
num.pop() #Remove o último valor da lista
num.pop(1) #Remove o valor da posição 1
del num[0] #Deleta o valor da posição 0
num.clear() #Limpa toda a lista

#Podemos criar usando o comando (if) para verificar se o elemento está na lista antes de remover
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = list(range(4, 11)) #Cria uma lista do 4 ao 10
print(valores)

valores = list(range(0, 11, 2)) #Cria uma lista do 0 ao 10 de 2 em 2
print(valores)


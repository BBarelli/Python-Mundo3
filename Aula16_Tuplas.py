'''
VARIÁVEIS COMPOSTAS (TUPLAS)
"AS TUPLAS SÃO IMUTÁVEIS" ELAS NÃO PODEM MUDAR!

A VARIÁVEL COMPOSTA PODE COMEÇAR DE 3 MANEIRAS: 
() - TUPLA
[] - LISTA
{} - DICIONÁRIO 

#PODE TER DADOS DE TIPOS DIFERENTES DENTRO DA TUPLA
# COMO FAZER PARA APAGAR UMA TUPLA -> (DEL nome_da_tupla)  

NA VERSÃO DO PYTHON DO MEU NOT, A TUPLA RODA SEM A PRESENÇA DOS PARENTESE, MAS POR PADRÃO IREI USAR ASSIM MESMO

EXEMPLOS DE TUPLAS:
*váriavel:
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

*pro sistema:
lanche = 0, 1, 2, 3


'''
# PRÁTICA

#TUPLA
def maneira1():
#TUPLA COM FOR
    lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
    for comida in lanche: #Saída o elemento em lanche
        print(f'{comida}')

def maneira2(): #Contagem do elemento
    lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
    for cont in range (0, len(lanche)):
        print(f'Eu vou comer {lanche[cont]} na posição {cont}')

def maneira3(): #No enumerate ele me dá a posição e o dado
    lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
    for pos, comida in enumerate (lanche): 
        print(f'Eu vou comer {comida} na posição {pos}')

maneira2()

#MOSTRA A TUPLA DE MODO ORDENADO
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(sorted(lanche)) #Mostra em ordem alfabética, mas não altera a tupla

#TUPLA COM NÚMEROS
def tuplaNumerica():
    a = (2, 4, 6)
    b = (1, 3, 5, 7)
    c = a + b #Junta as tuplas 
    print(c)
    #tem a opção de contar o comprimento da tupla
    print(len(c))  
    #tem a opção de contar a ocorrência de um elemento
    print(c.count(2))
    #tem a opção de encontrar a posição de um elemento
    print(c.index(2))   


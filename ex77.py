'''
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
 Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

palavras = ('Banana', 'Abacaxi', 'Laranja', 'Uva', 'Morango', 'Pera', 'Manga', 'Melancia')
for vogais in palavras:
    print(f'\nNa palavra {vogais} temos: ', end='')
    for letra in vogais:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')   
print('\nFim do programa')
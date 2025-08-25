'''
Exercício Python 73:
 Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
'''
from ast import If


print('-'*30)
print('Tabela do Brasileirão Betano 2025')
print('-'*30)

tabela = (
'Flamengo','Cruzeiro','Palmeiras','Bahia','Botafogo','Mirassol','São Paulo','Bragantino','Fluminense','Ceará SC'
'Corinthians','Atlético-MG','Internacional','Grêmio','Santos','Vasco da Gama','EC Vitória','Juventude',
'Fortaleza','Sport Recife')

print('''
      1 - Acessar ao G5 do campeonato.
      2 - Acessar ao Z4 do campeonato
      3 - Nomes em Ordem Alfabetica
      4 - Em que posição está o time do Santos.
      
      ''')

while True:
    opcao = int(input('Digite qual opção você deseja acessar: '))
    if opcao == 1:
        print(f'O G5 é formado por: {tabela[0:5]}')
    if opcao == 2:
        print(f'O Z4 é formado por: {tabela[-4:]}')
    if opcao == 3:
        print(sorted(tabela))
    if opcao == 4:
        print(f'{tabela[14]}')  

    cont = input('Deseja continuar: [S/N]: ').strip().upper()
    if cont == 'N':
        break
print('Fim do programa')
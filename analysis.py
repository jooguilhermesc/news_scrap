import csv

'''
THIS CODE SEARCH FOR A TERM AND RETURN HOW MANY TIMES THIS TERM WAS FOUND
'''

arquivo = open('noticias.csv')

linhas = csv.reader(arquivo)
i = 0

for linha in linhas:
    if 'CHOOSE_YOUR_OWN_TERM' in linha[0]:
        print(linha)
        i += 1

print(f'O termo "CHOOSE_YOUR_OWN_TERM" aparece em {i} notícias')

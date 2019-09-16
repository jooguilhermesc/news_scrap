import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import csv

subject_list = ['verdadeiro','impreciso','exagerado','distorcido','contraditorio','insustentavel','falso']
link = ''
n = 0
i = 0

f = csv.writer(open('CHOOSE_YOUR_FILE_NAME.csv','w'))
f.writerow(['Manchetes','Links']) #HERE YOU DEFINE WHAT IS THE NAME OF COLUMNS 

for i in range(0,5):
    link = 'https://aosfatos.org/noticias/checamos/' + subject_list[i]
    pagina = requests.get(link)
    soup = BeautifulSoup(pagina.content,'html.parser')
    for n in range(0,14):
        manchete = soup.find_all('h2')[n].get_text()
        new_link = soup.find_all('a', class_='card third')[n].get('href')
        f.writerow([manchete,new_link])

    sleep(3)

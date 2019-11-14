import re
import os
from tqdm import tqdm
from bs4 import BeautifulSoup

fips = open('test.html','r',encoding='utf-8')
#soup=BeautifulSoup(fips, 'lxml')

#забирает только строки с цифрами и более 5 знаков
def pn_to_list(f):
    soup=BeautifulSoup(f, 'lxml')
    strings = soup.find_all(string=re.compile('^[0-9]\d{5,20}'))
    pn_list = ''
    for txt in strings:
        #pn_list.append(" ".join(txt.split()))
        pn_list = pn_list + ("".join(txt.split())) + ';' + '\n'
    return pn_list    
#print(pn_list)

def from_html_to_csv():
    #папка с html файлами    
    path = 'H:/Работа2/09.19.Патенты Города (Стрельцова)/FIPS_html/msk_2016'
    os.chdir(path)

    pn_to_list_all = []
    for filename in tqdm(os.listdir(path)):
        if filename.endswith('.html'):
            with open(filename, 'r',encoding='utf-8') as f:
                pn_to_list_all.append(pn_to_list(f))
                #print(pn_to_list(f))
            f.close()
    #print(pn_to_list_all)
    with open('output' + '.csv', 'a') as nf:
        for i in pn_to_list_all:
            nf.write(i)

from_html_to_csv()
#print(pn_to_list(fips))           
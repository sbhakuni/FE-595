# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 23:53:13 2019

@author: bhaku
"""


from bs4 import BeautifulSoup
import pandas as pd
import requests

if __name__ == '__main__':
    male_text=[]
    female_text=[]
    for i in range(0,51,1):
        page = requests.get("https://theyfightcrime.org/")
        page.status_code    
        soup = BeautifulSoup(page.content, 'html.parser')
        soup.find_all('p')
        combined_text=soup.find_all('p')[1].get_text()
        text_list=[x for x in map(str.strip, combined_text.split('.')) if x]
        
        male_text.append(text_list[0])
        female_text.append(text_list[1])
        i+=1
    f= open("MaleHeroes1.txt","a+")
    g= open("FemaleHeroes1.txt","a+")
    
    with open('MaleHeroes1.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % place for place in male_text)
    with open('FemaleHeroes1.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % place for place in male_text)

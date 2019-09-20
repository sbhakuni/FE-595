# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 23:53:13 2019

@author: bhaku
"""

#from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests

for i in range(0,50,1):
    page = requests.get("https://theyfightcrime.org/")
    page.status_code
    #content=page.content
    #driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    #lenghty way of seperating text but usefull for complicated stuff
    """soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify())
    a=list(soup.children)
    [type(item) for item in list(soup.children)]
    html = list(soup.children)[0]
    list(html.children)
    [type(item) for item in list(html.children)]#it shows two tags one is head the second one is body
    body = list(html.children)[3]
    list(body.children)
    [type(item) for item in list(body.children)]
    final_body=list(body.children)[3]
    [type(item) for item in list(final_body.children)]
    text=list(final_body.children)[1]
    text.get_text()..."""
    
    soup = BeautifulSoup(page.content, 'html.parser')
    soup.find_all('p')
    combined_text=soup.find_all('p')[1].get_text()
    text_list=[x for x in map(str.strip, combined_text.split('.')) if x]
    """the above line of code seperates the sentences according to the use of the sentence breaker
    because in almost all of the iterations the male and female characters are distinguishable by first and 
    second line.We cannot manipulate our code by looking into the a large number of iteration before writing the code.
    thus i used combined_text.split('.')) only which corresponds to most cases.But in some cases there were no full stop
    between male and female characters,similarly there might be different issues with some iteration as we further iterate.
    data inconsistency cant be handle in this case"""
    male_text=text_list[0]
    female_text=text_list[1]
    
    f= open("MaleHeroes.txt","a+")
    f.write(f"\n{male_text}")
    
    g= open("FemaleHeroes.txt","a+")
    g.write(f"\n{female_text}")
    i+=1
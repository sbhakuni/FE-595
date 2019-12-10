# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:25:26 2019

@author: bhaku
"""

import os, zipfile,glob
from collections import Counter
import sys
from os.path import join, abspath, realpath, dirname

import os
from textblob import TextBlob   
import pandas as pd  

dir_name = os.path.dirname(os.path.abspath('__file__'))
print (dir_name)

extension = ".zip"

zip_files = glob.glob('*.zip')

for zip_filename in zip_files:
    dir_name = os.path.splitext(zip_filename)[0]
    os.mkdir(dir_name)
    zip_handler = zipfile.ZipFile(zip_filename, "a")
    zip_handler.extractall(dir_name)
 #delete zip files after extraction
'''for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.abspath(item) # get full path of files
        os.remove(file_name) # delete zipped file'''


for item in os.path.dirname("__file__"):
    if item.endswith(".zip"):
        os.remove(os.path.join(dir_name, item))

t_path=[]    
for path, subdirs, files in os.walk(dir_name):
    
    for name in files:
        #text_path=[]
        t_path.append(os.path.join(path, name))    
        print(name)

term = "__MACOSX" # AS MAC OS GIVES ADDITIONAL FILES WHILE ZIPPING WHICH ARE NOT ENCODED PROPERLY.WE WILL REMOVE IT
index=[]
for i,x in enumerate(t_path):
    words = x.split('\\\\') #split the sentence into individual words

    if term in words: #see if one of the words in the sentence is the word we want
        t_path.pop(i)
    
term = "__MACOSX" # AS MAC OS GIVES ADDITIONAL FILES WHILE ZIPPING WHICH ARE NOT ENCODED PROPERLY.WE WILL REMOVE IT
index=[]
for i,x in enumerate(t_path):
    words = x.split('\\\\') #split the sentence into individual words

    if term in words: #see if one of the words in the sentence is the word we want
        t_path.pop(i)
        

with open("result.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
she='She\'s'
he='He\'s'
for i in content:
    if i.find('She')is not -1: 
         file= open("FemaleOutput.txt", 'a')
         file.write(f"{i}\n")

    elif i.find('He')is not -1:
         file= open("MaleOutput.txt", 'a')
         file.write((f"{i}\n"))

#   Sentiment analysis
#for male heroes
from textblob import TextBlob   
import pandas as pd    
fh = open('MaleOutput.txt')

def maledf(textfile):
    #fh = open(textfile)
    df_male=pd.DataFrame()
    
    df_male = pd.read_csv(textfile, sep="\n", header=None)
    df_male.columns=["Text"]
    df_male["textblob"]=df_male["Text"].apply(lambda x:TextBlob(x)) 
    df_male["polarity"]=df_male["textblob"].apply(lambda x :x.sentiment[0])
    df_male["subjectivity"]=df_male["textblob"].apply(lambda x :x.sentiment[1])
    return df_male
df_male=maledf('MaleOutput.txt')
def femaledf(textfile):
    #fh = open(textfile)
    df_female=pd.DataFrame()
    
    df_female = pd.read_csv(textfile, sep="\n", header=None)
    df_female.columns=["Text"]
    df_female["textblob"]=df_female["Text"].apply(lambda x:TextBlob(x)) 
    df_female["polarity"]=df_female["textblob"].apply(lambda x :x.sentiment[0])
    df_female["subjectivity"]=df_female["textblob"].apply(lambda x :x.sentiment[1])
    return df_female

df_female=femaledf('FemaleOutput.txt')
df_male=df_male.sort_values(by='polarity', ascending=False)
df_female=df_female.sort_values(by='polarity', ascending=False)

Top10_positive_male=df_male.head(10)

df_male=df_male.sort_values(by='polarity')
Top10_negative_male=df_male.head(10)

Top10_positive_female=df_female.head(10)

df_female=df_female.sort_values(by='polarity')
Top10_negative_female=df_female.head(10)

# Python program to find the k most frequent words 
   
def Counter1(filename):
    with open(filename, 'r') as file:
        datastring = file.read().replace('\n', '')
    # split() returns list of all the words in the string 
        
    blob=TextBlob(datastring)
    qaz=blob.noun_phrases
    
    decriptors_series=[]
    for i in range(0,len(qaz)):    
        decriptors_series.append(qaz[i])         
    Counter = Counter(decriptors_series) 
    most_occur = Counter.most_common(10) 
    return most_occur 

a=Counter1('result.txt')
print(a)


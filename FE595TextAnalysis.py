#!/usr/bin/env python
# coding: utf-8

# SHAANTANU BHAKUNI

# (1) Used the results of the web scrappers made by individual students in the class to clean the data.
# All results of Male and female characters were put in different text file and then analysis was dne on them

# In[1]:


import os, zipfile,glob

dir_name = 'C:\\Users\\bhaku\\Desktop\\allheroesJ'
extension = ".zip"
os.chdir(dir_name)
#unzip all files
zip_files = glob.glob('*.zip')

for zip_filename in zip_files:
    dir_name = os.path.splitext(zip_filename)[0]
    os.mkdir(dir_name)
    zip_handler = zipfile.ZipFile(zip_filename, "a")
    zip_handler.extractall(dir_name)
    
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".zip"):
        os.remove(os.path.join(dir_name, item))

text_path=[]    
for path, subdirs, files in os.walk(dir_name):
    
    for name in files:
        #text_path=[]
        text_path.append(os.path.join(path, name))    
        #print(name)
t_path = [w.replace( '\\' , '\\\\' ) for w in text_path]#backlash changed for putting in directory


  
term = "__MACOSX" # AS MAC OS GIVES ADDITIONAL FILES WHILE ZIPPING WHICH ARE NOT ENCODED PROPERLY.WE WILL REMOVE IT
index=[]
for i,x in enumerate(t_path):
    words = x.split('\\\\') #split the sentence into individual words

    if term in words: #see if one of the words in the sentence is the word we want
        t_path.pop(i)
    
term = "__MACOSX" # AS MAC OS GIVES ADDITIONAL FILES WHILE ZIPPING WHICH ARE NOT ENCODED PROPERLY.WE WILL REMOVE IT
index=[]
for i,x in enumerate(t_path):
    words = x.split('\\\\') #split the sentence into individual words based on \\

    if term in words: #see if one of the words in the sentence is the word we want
        t_path.pop(i)
        
with open("result.txt", 'w') as outfile:
    for fname in t_path:
        with open(fname) as infile:
            outfile.write(infile.read())   

           
with open("result.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
for i in content:
    if i.find('She')is not -1: 
         file= open("FemaleOutput.txt", 'a')
         file.write(f"{i}\n")

    elif i.find('He')is not -1:
         file= open("MaleOutput.txt", 'a')
         file.write((f"{i}\n"))


# (3) Sentiment analysis after cleaning the files(using textblob)

# In[2]:


#   Sentiment analysis
#for male heroes
from textblob import TextBlob   
import pandas as pd    
fh = open('MaleOutput.txt')
df_male=pd.DataFrame()
for line in fh:
    print(line)
fh.close()
df_male = pd.read_csv('MaleOutput.txt', sep="\n", header=None)
df_male.columns=["Text"]
    
    
df_male["textblob"]=df_male["Text"].apply(lambda x:TextBlob(x)) 
df_male["polarity"]=df_male["textblob"].apply(lambda x :x.sentiment[0])
df_male["subjectivity"]=df_male["textblob"].apply(lambda x :x.sentiment[1])

#for female heroes
fh = open('FemaleOutput.txt')
df_female=pd.DataFrame()
for line in fh:
    print(line)
fh.close()
df_female = pd.read_csv('FemaleOutput.txt', sep="\n", header=None)
df_female.columns=["Text"]
    
    
df_female["textblob"]=df_female["Text"].apply(lambda x:TextBlob(x)) 
df_female["polarity"]=df_female["textblob"].apply(lambda x :x.sentiment[0])
df_female["subjectivity"]=df_female["textblob"].apply(lambda x :x.sentiment[1])

df_male=df_male.sort_values(by='polarity', ascending=False)
df_female=df_female.sort_values(by='polarity', ascending=False)

Top10_positive_male=df_male.head(10)

df_male=df_male.sort_values(by='polarity')
Top10_negative_male=df_male.head(10)

Top10_positive_female=df_female.head(10)

df_female=df_female.sort_values(by='polarity')
Top10_negative_female=df_female.head(10)


# In[11]:


Top10_positive_male=Top10_positive_male.drop(columns=["textblob"])
Top10_negative_male=Top10_negative_male.drop(columns=["textblob"])
Top10_positive_female=Top10_positive_female.drop(columns=["textblob"])
Top10_negative_female=Top10_negative_female.drop(columns=["textblob"])


# In[13]:


print("Top 10 positive male characters are:")
Top10_positive_male


# In[14]:


print("Top 10 negative male characters are:")
Top10_negative_male


# In[15]:


print("Top 10 positive female characters are:")
Top10_positive_female


# In[16]:


print("Top 10 negative  female characters are:")
Top10_negative_female


# (4)find the top 10 descriptors with their frequency 

# In[17]:


from collections import Counter 

with open('result.txt', 'r') as file:
    datastring = file.read().replace('\n', '')
# split() returns list of all the words in the string 
    
blob=TextBlob(datastring)
qaz=blob.noun_phrases

decriptors_series=[]
for i in range(0,len(qaz)):    
    decriptors_series.append(qaz[i])
    

Counter = Counter(decriptors_series)
# most_common() produces k frequently encountered 
# input values and their respective counts. 
most_occur = Counter.most_common(10) 
  
print(most_occur)


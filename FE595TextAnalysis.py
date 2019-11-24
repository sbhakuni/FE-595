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
#have to do it twice because of the format of macosx  
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
file= open("FemaleOutput.txt", 'a')
file1= open("MaleOutput.txt", 'a')
for i in content:
    if i.find('She')is not -1: 
         file.write(f"{i}\n")

    elif i.find('He')is not -1:
         file1.write((f"{i}\n"))
            
            
#   Sentiment analysis
#for male heroes
from textblob import TextBlob   
import pandas as pd    
fh = open('MaleOutput.txt')
df_male=pd.DataFrame()
df_male = pd.read_csv('MaleOutput.txt', sep="\n", header=None)
df_male.columns=["Text"]
    
    
df_male["textblob"]=df_male["Text"].apply(lambda x:TextBlob(x)) 
df_male["polarity"]=df_male["textblob"].apply(lambda x :x.sentiment[0])
df_male["subjectivity"]=df_male["textblob"].apply(lambda x :x.sentiment[1])

#for female heroes
fh = open('FemaleOutput.txt')
df_female=pd.DataFrame()

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

Top10_positive_male=Top10_positive_male.drop(columns=["textblob"])
Top10_positive_male.drop_duplicates(subset ="Text", 
                     keep = False, inplace = True) 
Top10_negative_male=Top10_negative_male.drop(columns=["textblob"])
Top10_positive_male.drop_duplicates(subset ="Text", 
                     keep = False, inplace = True) 
Top10_positive_female=Top10_positive_female.drop(columns=["textblob"])
Top10_positive_female.drop_duplicates(subset ="Text", 
                     keep = False, inplace = True) 
Top10_negative_female=Top10_negative_female.drop(columns=["textblob"])
Top10_positive_female.drop_duplicates(subset ="Text", 
                     keep = False, inplace = True) 


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
 
most_occur = Counter.most_common(10) 
# input values and their respective counts.  
print(most_occur)

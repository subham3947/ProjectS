from newspaper import Article
import os
path="/home/nakul/*****/ProjectS/DATA/ET/JULY/"
l=os.listdir(path)
for i in l:
    file=open(path+i,"r")
    fname=i.split('.')
    fname=fname[0]+"_all_article.txt"
    wfile = open(fname,"a",encoding='utf-8')
    for line in file:
        
        try:
            article = Article(line[:-1],language='en')
            article.download()
            article.parse()
            text=article.text  
        except:
            print('Link expired!!')
            continue
         
        wfile.write(text+'\n')
        print('write')
    wfile.close()

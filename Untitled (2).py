
# coding: utf-8

# In[ ]:

from newspaper import Article
import os
path="/home/nakul/Downloads/ProjectS-master/ET/JULY/"
l=os.listdir(path)
for i in l:
    file=open(path+i,"r")
    for line in file:
        
        try:
            article = Article(line[:-1],language='en')
            article.download()
            article.parse()
            text=article.text
            print(text)
            #file = open(fname,"w",encoding='utf-8') 
            #file.write(first_article.text) 
        except:
            continue
        
    file.close()


# In[18]:

from newspaper import Article
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
article = Article("https://economictimes.indiatimes.com/small-biz/startups/gst-how-startups-have-prepared-themselves-for-the-new-tax-regime/articleshow/59398109.cms",language='en')
article.download()
article.parse()
stop_words = set(stopwords.words('english'))
print(article.text)
word_tokens = word_tokenize(article.text.lower())
filtered_sentence = [w for w in word_tokens if not w in stop_words]
para=""
for w in filtered_sentence:
    para=para+" "+w
lines=para.split('.')
wfile = open("testfile.txt","w") 
wfile.write(str(lines))


# In[ ]:




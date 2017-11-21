
# coding: utf-8

# In[7]:


from newspaper import Article
f = open("link.txt","r")
for line in f.readlines():
    l=line.split('|')
    fname,url=l[0]+".txt",l[1]
    first_article = Article(url[:-1],language='en')
    first_article.download()
    first_article.parse()
    file = open(fname,"w",encoding='utf-8') 
    file.write(first_article.text) 
    file.close()
f.close()


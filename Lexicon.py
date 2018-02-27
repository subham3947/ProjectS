
# coding: utf-8

# In[76]:

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from nltk import sent_tokenize,word_tokenize,pos_tag,FreqDist
from collections import Counter


# In[23]:

f = open("C:/Users/NAKUL/Desktop/01-07-2017_all_article.txt", "r",encoding="utf8")
s=f.read()
#remove punctuations
doc=''
punctuations = '''!()-[]{};:'"“”\,<>./?@#$%^&*_~'''
for char in s.lower():
   if char not in punctuations:
       doc = doc + char


# In[86]:

#finding POS and Frequency Distribution
all_words=word_tokenize(doc)

pos_tagged=pos_tag(words)
lex_words=[]
for w,tag in pos_tagged:
    if tag.startswith('J') or tag.startswith('N') or tag.startswith('R') or tag.startswith('V'):
        lex_words.append(w)
#print(lex_words)
pos_tagged=pos_tag(lex_words)
#finding frequency distribution
Freqdist=dict(Counter(lex_words))
print(Freqdist)
freq_set=set()
for w in Freqdist:
    freq_set.add(Freqdist[w])
freq_set=sorted(freq_set,reverse=True)
freq_set=list(freq_set)
#find rank
rank={}  
for k,v in Freqdist.items():
    rank[k]=freq_set.index(v)+1
print(rank)


# In[92]:

wfile = open("samplelexicon.txt","a",encoding='utf-8')
for word, tag in pos_tagged:
   rf=rank[word]*Freqdist[word]
   synsets = wn.synsets(word)
   if not synsets:
       continue

           # Take the first sense, the most common
   synset = synsets[0]
   swn_synset = swn.senti_synset(synset.name())
   modified_pos_score=(1/(rf))+swn_synset.pos_score() 
   modified_neg_score=(1/(rf))+swn_synset.neg_score()
   print(modified_pos_score,modified_neg_score)
   synsets = wn.synsets(word)
   if not synsets:
         continue
   #print(synsets)
   wfile.write(word+'\t'+str(modified_pos_score)+'\t'+str(modified_neg_score)+str(synsets[0].name)+'\n')        
           


# In[ ]:




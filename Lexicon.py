
# coding: utf-8

# In[5]:

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from nltk import sent_tokenize,word_tokenize,pos_tag,FreqDist
from collections import Counter
lemmatizer = WordNetLemmatizer()


# In[6]:

senti_words = []
delimiter = " "
with open("C:/Users/NAKUL/Desktop/SentiWordNet_3.0.0_20130122.txt","r",encoding="utf-8") as f:
    for line in f:
        w=line.split('\t')[4]
        #print(w)
        i=w.index('#')
        #print(i)
        senti_words.append(w[:i])


# In[46]:

f = open("C:/Users/NAKUL/Desktop/01-07-2017_all_article.txt", "r",encoding="utf8")
s=f.read()
words=word_tokenize(s.lower())
lex_words=set()
for w in words:
    if w in senti_words:
        lex_words.add(w)
    else:
        continue


# In[48]:

def convert_tag(tag):
    
    if tag.startswith('J'):
        return wn.ADJ
    elif tag.startswith('N'):
        return wn.NOUN
    elif tag.startswith('R'):
        return wn.ADV
    elif tag.startswith('V'):
        return wn.VERB
    return None


# In[49]:

#find frequency distribution
Freqdist=dict(Counter(words))
#print(Freqdist)
freq_set=set()
for w in Freqdist:
    freq_set.add(Freqdist[w])
freq_set=sorted(freq_set,reverse=True)
freq_set=list(freq_set)
#print(freq_set)
#find rank
rank={}  
for k,v in Freqdist.items():
    rank[k]=freq_set.index(v)+1


# In[50]:

tagged_words=pos_tag(list(lex_words))
wfile = open("samplelexicon.txt","a",encoding='utf-8')
for word, tag in tagged_words:
        rf=rank[word]*Freqdist[word]
        wn_tag = convert_tag(tag)
        if wn_tag not in (wn.NOUN, wn.ADJ, wn.ADV,wn.VERB):
            continue
    
        synsets = wn.synsets(word)
        if not synsets:
            continue
        synonyms=''
        for s in synsets:
            synonyms+='#'+s.lemmas()[0].name()
            # Take the first sense, the most common
        synset = synsets[0]
        swn_synset = swn.senti_synset(synset.name())
        modified_pos_score=(1/(rf))+swn_synset.pos_score() 
        modified_neg_score=(1/(rf))+swn_synset.neg_score()
        wfile.write(wn_tag+'\t'+word+'\t'+str(modified_pos_score)+'\t'+str(modified_neg_score)+'\t'+synonyms+'\n')
print('write complete')
wfile.close()


# In[ ]:




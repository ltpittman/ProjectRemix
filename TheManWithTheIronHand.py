
# coding: utf-8

# In[3]:


import random 
from textblob import TextBlob

with open('TheManWithTheIronHand.txt','r') as file:
    text = file.read()
    
blob = TextBlob(text)

nouns = []
adjectives = []
verbs = []

for word,pos in blob.tags:
    # print(word,pos)
    if (pos == 'JJ'):
        adjectives.append(word)
    if (pos == 'NN'):
        nouns.append(word)
    if (pos == 'BV'):
        verbs.append(word)

for i in range(18):
    a = random.choice(adjectives)
    n = random.choice(nouns)
    vb = random.choice(verbs)
    print(a,n)


# In[18]:


print(nouns)


# In[17]:


print(adjectives)


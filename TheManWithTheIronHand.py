
# coding: utf-8

# In[3]:


import random 
from textblob import TextBlob

#now enter your file that you plan on using... for me it would be "TheManWithTheIronHand"
with open('TheManWithTheIronHand.txt','r') as file:
    text = file.read()
    
blob = TextBlob(text)

#now create two emtpy lists for nouns and adjectives
nouns = []
adjectives = []

for word,pos in blob.tags:
    # print(word,pos)
    if (pos == 'JJ'):
        adjectives.append(word)
    if (pos == 'NN'):
        nouns.append(word)
        
# This generates an eighteen-line poem by pairing a random adjective 
for i in range(18):
    a = random.choice(adjectives)
    n = random.choice(nouns)
    print(a,n)


# In[18]:


print(nouns)


# In[17]:


print(adjectives)


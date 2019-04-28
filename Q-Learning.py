#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
import random

data = pd.read_csv('DataTugas3ML2019.txt',sep = '\t',header = -1)
pd.set_option("display.max_columns", 225)
pd.set_option('display.max_colwidth', 10000)
data


# # Penentuan Tabel Q

# In[238]:


def PossibleA(x,y):
    if (y == 0) and (x==0):
        arah = ['S','E']
        
    elif (y == 0) and (x==14):
        arah = ['S','W']
        
    elif (y == 14) and (x==0):
        arah = ['N','E']
        
    elif (y == 14) and (x==14):
        arah = ['N','W']
        
    elif (x==0):
        arah = ['N','S','E']
        
    elif (x==14):
        arah = ['N','S','W']
        
    elif (y==0):
        arah = ['S','E','W']
        
    elif(y==14):
        arah = ['N','E','W']
        
    else:
        arah = ['N','S','E','W']
        
    return arah


# In[239]:


def jalan(arah):
#     print(x,y)
#     print(arah)
    if(arahsblm == 'N'):
        arah.remove('S')
    elif(arahsblm == 'S'):
        arah.remove('N')
    elif(arahsblm == 'E'):
        arah.remove('W')
    elif(arahsblm == 'W'):
        arah.remove('E')
        
    return arah


# In[240]:


def pemilihanjalan(x,y,arah):
    index = x + y*15
    random.shuffle(arah)
    if (arah[0] == 'N'):
        TabelQ[index]['N'] = TabelQ[index]['N']+(alfa*(data[x][y-1]+gamma*max(TabelQ[index-15])-TabelQ[index]['N']))
        y-=1
    elif (arah[0] == 'S'):
        TabelQ[index]['S'] = TabelQ[index]['S']+(alfa*(data[x][y+1]+gamma*max(TabelQ[index+15])-TabelQ[index]['S'])) 
        y+=1
    elif(arah[0] == 'W'):
        TabelQ[index]['W'] = TabelQ[index]['W']+(alfa*(data[x-1][y]+gamma*max(TabelQ[index-1])-TabelQ[index]['W']))
        x-=1
    else:
        TabelQ[index]['E'] = TabelQ[index]['E']+(alfa*(data[x+1][y]+gamma*max(TabelQ[index+1])-TabelQ[index]['E']))
        x+=1
#     print(arah[0])
    return x,y,arah[0]


# In[405]:


TabelQ = []

for i in range(225):
    TabelQ.append([0.0,0.0,0.0,0.0,])

TabelQ = pd.DataFrame(TabelQ,columns = ['N','S','E','W'])
TabelQ = TabelQ.T

TabelQ


# In[406]:


alfa = 1
gamma = 0.8
x = 0
y = 14
arahsblm = ''

for episode in range (500):# jika pada saat hasil akhir di run tidak kluar hasilnya silahkan perbesar episodenya
    x = 0
    y = 14
    arahsblm = ''
    for i in range(200):
        arah = PossibleA(x,y)
        arah = jalan(arah)
        x,y,arahsblm = pemilihanjalan(x,y,arah)
TabelQ


# # Penentuan arah jalan

# In[407]:


def PossibleA2(x,y,arah):
    cek = False
    temp1,temp2 = [],[]
    for i in (arah):
        if (i == 'N') :
            temp1.append([x,y-1,'N'])
        elif(i == 'S'):
            temp1.append([x,y+1,'S'])
        elif(i == 'E'):
            temp1.append([x+1,y,'E'])
        elif(i == 'W'):
            temp1.append([x-1,y,'W'])
            
    for i in range(len(temp1)):
        for j in state:
            if (j[0] == temp1[i][0]) and (j[1] == temp1[i][1]):
                for k in temp2:
                    if temp1[i][2] == k:
                        cek = True
                if cek != True:
                    temp2.append(temp1[i][2])
     
    if len(temp2) != len(arah):
        for i in (temp2):
            arah.remove(i)

    return arah


# In[408]:


def maxTabel(x,y,arah,total,total2):
    index = x + y*15
    nomor.append(index)
#     print(index)
    temp = []
#     print(arah)
    for i in (arah):
        temp.append(TabelQ[index][i])
#     print temp
    hasil = max(temp)
    total2.append([index,data[x][y]])
    total += data[x][y]
    temp = []
    for i in (arah):
#         print i
        if TabelQ[index][i] == hasil:
            temp.append(i)
            
    random.shuffle(temp) 
    if temp[0] == 'N' :
        perjalanan.append([index,'N',index-15])
        y-=1
    elif temp[0] == 'S' :
        perjalanan.append([index,'S',index+15])
        y+=1
    elif temp[0] == 'E' :
        perjalanan.append([index,'E',index+1])
        x+=1
    elif temp[0] == 'W' :
        perjalanan.append([index,'W',index-1])
        x-=1
    return x,y,total,total2


# # Hasil Akhir 

# In[409]:


x = 0
y = 14
total= 0
state,total2 = [],[]
perjalanan,nomor = [],[]
while (x!=14) or (y!=0):
    state.append([x,y])
    arah = PossibleA(x,y)

    arah = PossibleA2(x,y,arah)

    x,y,total,total2 = maxTabel(x,y,arah,total,total2)

total = total + 500

print('Titik Akhir ',x,y)
print('Total Reward',total)



# In[410]:


t = pd.DataFrame(total2).T
header = t.iloc[0]
t = t[1:]
t = t.rename(columns = header)
t


# In[411]:


df = pd.DataFrame(perjalanan).T

header = df.iloc[0]
df = df[1:]
df = df.rename(columns = header)
df


# In[ ]:





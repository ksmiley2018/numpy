#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


np.__version__


# In[4]:


array1=np.array([1,2,3])
array1


# In[5]:


type(array1)


# In[8]:


array2=np.array([
                  [1,2],
                  [3,4]
])
array2


# In[10]:


array2d=np.array([
                  [1,2,3.3],
                  [4,5,6.6]    
])
array2d


# In[14]:


arrex=np.array([
                [
                 [1,2],
                 [3,4]
               ],
               [
                   [5,6],
                   [7,8]
               ]
])
arrex


# In[15]:


array3=np.array([
                [
                   [1,2,3],
                   [4,5,6],
                   [7,8,9]
                ],
                  [
                      [10,11,12],
                      [13,14,15],
                      [16,17,18]
                  ]
])
array3


# In[16]:


array4=np.array((12,13,14))
array4


# In[17]:


print(array1.ndim)


# In[18]:


print(array2.ndim)


# In[19]:


print(array4.ndim)


# In[20]:


print(array3.ndim)


# In[21]:


array5=np.array([1,2,3,4],ndmin=4)
array5


# In[22]:


array5.shape


# In[23]:


array1.shape


# In[24]:


array2.shape


# In[25]:


array3.shape


# In[26]:


array4.shape


# In[27]:


array2


# In[29]:


array2d[0][1]


# In[ ]:





# In[30]:


array2d[1][0]


# In[32]:


array2d[0][2]


# In[33]:


for x in range(0,2):
    for y in range(0,3):
        print(array2d[x][y])


# In[34]:


array1.dtype


# In[35]:


array2d.dtype


# In[37]:


array5=np.array([1,2,3,4,5],dtype='S')


# In[38]:


array5


# In[40]:


array2dconv=array2d.astype('i')
array2dconv


# In[41]:


array2dconv=array2d.astype('f')
array2dconv


# In[42]:


numone=np.ones((2,2),dtype=int)
numone


# In[43]:


num=np.ones(3)
num


# In[44]:


num3d=np.ones((2,3,3))
num3d


# In[46]:


numszero=np.zeros((3,2),dtype=int)
numszero


# In[47]:


range_array=np.arange(0,10,3)
range_array


# In[50]:


a=np.random.randint(low=1,size=5)
a


# In[51]:


b=np.random.randint(low=1,high=6,size=(2,3))
b


# In[52]:


np.concatenate([array1,array4])


# In[53]:


flatarr=array3.flatten()
flatarr


# In[54]:


np.reshape(flatarr[:4],(2,2))


# In[55]:


flatarr[:4]


# In[56]:


np.eye(2)


# In[57]:


np.eye(3)


# In[58]:


np.eye(3,dtype=int)


# In[60]:


import pandas as pd
df=pd.DataFrame(array2d)
df


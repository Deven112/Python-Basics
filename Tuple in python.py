#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Tuple : 
    1.immutable=> No method to add update and delete in same memory location
    2.Ordered => indexing and slicing 
    3.Heterogenious
    


# In[2]:


t = (10,20,30,40,50)

print(type(t))


# In[38]:


a = 10,20

print(a)

print(type(a))


# In[8]:


b = (10) 

print(type(b))

b = (10,)
print(type(b))


# In[39]:


b = 100,200

print(a,b)
print(type(b))


# In[16]:


print(dir(tuple))


# In[20]:


# Count and Index =>
t = (10,20,30,40,50,60,70,80,90,100)

print(t.count(100))
print(t.index(100))


# In[24]:


t = (10,20,30,40,50,60,70,80,90,100)

print(t[0])
print(t[-1])


# In[27]:


t = (10,20,30,40,50,60,70,80,90,100)

print(t[0:5])

print(t[0:9:2])


# In[33]:


t = (10,20,30,40,50,60,70,80,90,100)

print(t[::-1])


# In[35]:


l = [10,20,30,40,50,60]

for index,value in enumerate(l):
    print(index,value)


# In[40]:


l = [10,20,30,40,50,60]

for d in enumerate(l):
    print(d)


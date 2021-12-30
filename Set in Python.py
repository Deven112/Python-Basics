#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Set: 
   1. Mutable => Add/update and delete in same memory location 
   2. Unordered => Not supported indexing and slicing 
   3. {10:None,20:None,30:None,40:None,50:None}
   4. All the elements in set should be unique
   5. All the elements in set should be immutable - int, string, float, tuple


# In[3]:


s ={10,20,10,20,30,40,50,50,60,70}

print(s)

print(type(s))


# In[50]:


s1 ={10,20,10,20,30,40,50,50,60,70}
print(s1)

p = sorted(s1)
print(p)


# In[9]:


s1 = {10,20,30,40,50,60}
s2 = {40,50,60,70,80,90}

s3 = s1.union(s2)
print(s3)


# In[11]:


s1 = {10,20,30,40,50,60}
s2 = {40,50,60,70,80,90}

s3 = s1.intersection(s2)
print(s3)


# In[54]:


s1 = {10,20,30,40,50,60}
s2 = {40,50,60,70,80,90}

s3 = s2.difference(s1)
print(s3)


# In[14]:


s1 = {10,20,30,40,50,60}
s2 = {40,50,60,70,80,90}

s3 = s1.symmetric_difference(s2)
print(s3)


# In[16]:


print(dir(set))


# In[18]:


s1 = {10,20,30,40,50,60}
s2 = {40,50,60,70,80,90}

s1.update(s2)
print(s1)


# In[20]:


s1 = {10,20,30,40,50,60}
s2 = {40,50,60,70,80,90}

s1.intersection_update(s2)
print(s1)


# In[22]:


s1 = {10,20,30,40,50,60}
s2 = {40,50,60,70,80,90}

s1.difference_update(s2)
print(s1)


# In[23]:


s1 = {10,20,30,40,50,60}
s2 = {40,50,60,70,80,90}

s1.symmetric_difference_update(s2)
print(s1)


# In[25]:


s1 = {10,20,30,40,50,60}

s1.add(100)

print(s1)


# In[27]:


s1 = {10,20,30,40,50,60}

print(s1[0])


# In[30]:


s1 = {10,20,30,40,50,60}

for value in s1:
    print(value)


# In[ ]:


Delete : 
    1.pop
    2.remove
    3.discard
    4.clear
    5.del
    


# In[35]:


s1 = {10,20,30,40,50,60}

s1.pop()

print(s1)


# In[57]:


s1 = {10,20,30,40,50,60}

s1.remove(20)

print(s1)


# In[58]:


s1 = {10,20,30,40,50,60}

s1.discard(300)

print(s1)


# In[42]:


s1 = {10,20,30,40,50,60}

s1.clear()

print(s1)


# In[47]:


l1 = [10,20,30,40,50,60,70]
l2 = [80,90,100,200,300,400,500,]

s1 = set(l1)
s2 = set(l2)
print(s1,s2)


# In[49]:


l1 = [10,20,30,40,50,60,70]
l2 = [80,90,100,200,300,400,500,]

s1 = set(l1)
s2 = set(l2)

s1.update(s2)
print(s1)


# In[ ]:





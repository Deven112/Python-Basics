#!/usr/bin/env python
# coding: utf-8

# In[ ]:


List:
    1.Mutable => add, update and delete in same memory location
    2.Ordered => indexing and slicing 
    3.Heterogenous => [10,30,"python",[1,2,3,4]]


# In[1]:


l = [10,20,30,40,50]
print(l)


# In[4]:


l = [10,20,30,40,50]

print(l[0])

print(l[1])


# In[7]:


l = [10,20,"python",30,40,50,"Java"]

print(l[2])

print(l[-1])


# In[8]:


l = [10,20,30,40,50,[1,2,3,4,5]]

print(l[-1])


# In[157]:


l=[10,20,30,40,50,[1,2,3,4,5]]

print(l[-1][2])


# In[159]:


l1 = [10,20,30,[100,200,300,[1000,2000,3000]]]

print(l1[-1][-1][1])


# In[183]:


l2 = [10,20,30,[100,200,300,[1000,2000,3000]]]

print(l2[0:2])

print(l2[::-1])


# In[184]:


l4 = [10,20,30,40,50,60,[100,200,300,[1000,2000,3000]]]

print(l4[0:5:2])


# In[173]:


l5 = [10,20,30,40,50,60,[100,200,300,400,500,600,[1000,2000,3000,4000,5000,6000]]]

print(l5[-1][-1][0:4])


# In[174]:


l5 = [10,20,30,40,50,60,[100,200,300,400,500,600,[1000,2000,3000,4000,5000,6000]]]
print(l5[-1][-1][0:5])


# In[ ]:


List : Mutable => add/upate/delete 

Functions for Add:
                 1.append
                 2.extend
                 3.insert
                 


# In[166]:


# Append =>

l6 = ["python","java","c++"]

l6.append("R")

print(l6)


# In[149]:


l6 = ["python","java","c++"]
print(id(l6))

l6.append("R")

print(l6)
print(id(l6))


# In[110]:


#Extend =>

l7= ["pyhton","java","c++"]
l8 = ["R","SAS","C#"]

l7.extend(l8)


print(l7)


# In[168]:


l8 = [100,200,300,400]

l8.insert(5,20)

print(l8)


# In[169]:


l9 = [[1,2,3],[4,5,6],[7,8,9]]

for value in l9:
    print(value)


# In[170]:


l9 = [1,2,3,4,5]

for value in l9:
    print(value)


# In[ ]:


Delete: 1. pop => By default remove last element 
        2. remove => delete value
        3.clear => clear all elements 
        4.del=>


# In[123]:


# pop =>

l10 = [10,20,30,40,50]

r = l10.pop()
print(r)

r = l10.pop(2)
print(r)


# In[171]:


# remove =>
l11 = [10,20,30,40,50]

r = l11.remove(30)
print(l11)


# In[131]:


l12 = [10,20,30,40,50]

r = l12.clear()
print(l12)


# In[133]:


print(dir(list))


# In[139]:


# Sort =>
l12 = [10,45,103,78,12]

l12.sort()

print(l12)


# In[145]:


#Index and Count =>

l12 = [10,45,103,78,12,45,78,13,12,16,45]

print(l12.index(103))

print(l12.count(45))


# In[146]:


l = [10,20,30,40,50,60]

for index,value in enumerate(l):
    print(index,value)


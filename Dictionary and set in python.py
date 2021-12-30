#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Dict : 1. Mutable => add/update/delete in same memory location
       2.Unordered => Not support indexing and slicing 
       3. Contain key and value in pair, All keys should be "unique"
       4. All the Keys should be immutable =>tuple, int, float , string, 


# In[12]:


d = {"name":"dev","age":45,"email":"abc@gmail.com","marks":[50,80,75,86,90]}

print(d)


# In[13]:


d = {"name":"dev","age":45,"email":"abc@gmail.com","email":"def@gmail.com"}

print(d)


# In[15]:


print(d["name"])
print(d["email"])
print(d["age"])


# In[17]:


# Adding element in dictionary =>

d = {"name":"dev","age":45,"email":"abc@gmail.com","marks":[50,80,75,86,90]}

d['id'] = 45

print(d)


# In[55]:


# Updating element in dictionary =>

d = {"name":"dev","age":45,"email":"abc@gmail.com","marks":[50,80,75,86,90]}
d['id'] = 45
print(d)
print(id(d))

d['id'] = 50
print(d)
print(id(d))


# In[24]:


print(dir(dict))


# In[ ]:


Functions : 1. Keys => all keys from dict
            2. Values => all valuse from dict
            3. Items => tuple(key, value )
            


# In[27]:


d = {"name":"dev","age":45,"email":"abc@gmail.com","marks":[50,80,75,86,90]}

print(d.keys())


# In[29]:


d = {"name":"dev","age":45,"email":"abc@gmail.com","marks":[50,80,75,86,90]}

print(d.values())


# In[31]:


d = {"name":"dev","age":45,"email":"abc@gmail.com","marks":[50,80,75,86,90]}

print(d.items())


# In[ ]:


Delete:
    1. pop => Keys
    2. popitem => It removes the last key and value pair
    3.Clear => Emplty dict
    4.del => delete the referance 
    


# In[35]:


d = {"name":"dev","age":45,"email":"abc@gmail.com","marks":[50,80,75,86,90]}
print(d.pop("name"))
print(d.pop("email"))


# In[38]:


d = {"name":"dev","age":45,"email":"abc@gmail.com","marks":[50,80,75,86,90]}
print(d.popitem())


# In[40]:


d = {"name":"dev","age":45,"email":"abc@gmail.com","marks":[50,80,75,86,90]}
print(d.clear())


# In[45]:


d = {"name":"dev","age":45,"email":"abc@gmail.com","marks":[50,80,75,86,90]}
del d
print(d)


# In[47]:


l1 = [1,2,3,4,5]
l2 = [1,4,9,16,25]

d = dict(zip(l1,l2))
print(d)


# In[51]:


l1 = [1,2,3,4,5,6,7]

d = dict.fromkeys(l1,5)

print(d)


# In[53]:


d1 = {1:1,2:4,3:9}
d2 = {4:16,5:25}

d1.update(d2)
print(d1)


# In[ ]:





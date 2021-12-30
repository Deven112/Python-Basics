#!/usr/bin/env python
# coding: utf-8

# In[ ]:


String - 
1. Immutable => No Method to add update and delete in the same memory location  
2. Ordered => Indexing and slicing 
3.'Pyhton' , "Java" , '''c++ '''


# In[120]:


s1 = "Pyhton"
print(id(s1))

s1 = "Python"
print(id(s1))


# In[5]:


s1 = "Python is easy to learn"
print(s1)


# In[9]:


s1 = "'pyhton' is easy to learn"
print(s1)


# In[11]:


s1 = '"pyhton" is easy to learn'
print(s1)


# In[14]:


s1 = "\"pyhton\" is easy to learn"
print(s1)


# In[17]:


s1 = '''pyhton 
is easy to learn'''
print(s1)


# In[ ]:


Index => Pick a specific charcter from  a string


# In[123]:


s1 = 'pyhton is easy to learn'
print(s1[0])
print(s1[1])


print(s1[-2])


# In[126]:


s1 = 'pyhton is easy to learn'
print(s1[0:6])

print(s1[:6])


# In[30]:


s1 = 'pyhton is easy to learn'
print(s1[7:10])

print(s1[7:])


# In[119]:


# Stride =>

s1 = 'pyhton_is_easy_to_learn'
print(s1[0::2])

print(s1[0::3])


# In[ ]:


Arithmatic Operaton on string


# In[40]:


s1 = "Python"
s2 = "Java"

print(s1+s2)

print(s1-s2) => Not supported 

print(s1*s2) => Not supported


# In[105]:


print(s1*2)
print(s1*3)


# In[104]:


Builtin Function directory for string
print(dir(str))


# In[51]:


help(str)


# In[54]:


# Format function- 
num1 = 100
num2 = 200
s1 = "the value for num1 is {} and value for num2 is {}".format(num1, num2)
print(s1)


# In[127]:


num1 = 100
num2 = 200

s1 = "the value of num is",num1 
print(s1)


# In[128]:


name = "Dev"
email = "abc@gmail.com"

s1 = "Recieved an entry from user {} with email {}".format(name, email)
print(s1)


# In[134]:


#Split and Join functions

# Split =>

s = "pyhton,java,c++,r"
l = s.split(",")
print(l)


# In[72]:


print(l[2])
print(l[3])


# In[135]:


# Join =>

l = ["hii","pyhton","students"]


s = (" ").join(l)
print(s)

s = ("#").join(l)
print(s)


# In[80]:


# Find , index, rfind, rindex, count functions 


# In[82]:


# Find => 

s = "pyhton,java,c++,r"
print(s.find("java"))


# In[84]:


# Index => 
s = "pyhton,java,c++,r"
print(s.index("java"))


# In[93]:


# rfind = >
s = "pyhton,java,c++,r,java"
print(s.rfind("c++"))


# In[136]:


# rindex = >
s = "pyhton, java, c++,r,java"
print(s.rindex("c++"))


# In[137]:


# Count =>

k= "hello,hello,pyhton,hello"
print(k.count("pyhton"))


# In[50]:


# lower, islower, upper, isupper, title, istitle, capatalize function 


# In[53]:


# lower => 
s= "Python String"
print(s.lower())


# In[138]:


# islower => 
s= "python string"
print(s.islower())


# In[57]:


# upper => 
s= "Python String"
print(s.upper())


# In[139]:


# isupper => 
s= "PYTHON"
print(s.isupper())


# In[61]:


# title => 
s = "PyThon sTring"
print(s.title())


# In[140]:


# istitle => 
s= "Python String"
print(s.istitle())


# In[66]:


# Capitalize => 
s= "PyThon sTring"
print(s.capitalize())


# In[67]:


# isalpha, isdigit, isalnum, isspace


# In[141]:


# isalpha =>
s = "1234"
print(s.isalpha())


# In[82]:


# isdigit =>
s = "Python"
p = "python,39"
k = "12345"

print(s.isdigit())
print(p.isdigit())
print(k.isdigit())


# In[86]:


# isalnum =>
s = "Python39"
print(s.isalnum())


# In[93]:


# isspace =>
s = " "
p = """

"""
print(s.isspace())
print(p.isspace())


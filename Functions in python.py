#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Syntex:

    def function_name(parameters Or arguments):
    [statements]
    


# In[37]:


def eveninggreet():
    print("Good evening!")
    
eveninggreet()


# In[38]:


def greet(name):
    print("Hello," + name + ".Good morning!")
    

greet('dev')


# In[39]:


def add(x,y):
    c = x+y
    print(c)
   

add(20,5)


# In[33]:


def sub(x,y):
    c = x-y
    print(c)

sub(10,5)


# In[41]:


def mult(x,y):
    c = x*y
    return c

c = mult(5,5)
print(c)


# In[16]:


def add_sub(x,y):
    c = x+y
    d = x-y
    return c,d

result1, result2 = add_sub(5,4)
print(result1 , result2)


# In[42]:


def mycal (x,y):
    add = x+y
    sub = x-y
    mult = x*y
    div = x/y
    return add, sub, mult, div
add,sub,mult,div = mycal(50,70)

mult


# In[43]:


# Function to check the number is even or not 

def CheckEven(num):
    if num % 2==0:
        return True 
    else:
        return False 

CheckEven(40)


# In[ ]:





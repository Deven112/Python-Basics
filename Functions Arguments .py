#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Function Arguments:
    
1.The difference between argument and parameter
2.Types of argument
  a. Default argument 
  b. Positional and keyward argument
  c. variable length argument 
3.Local vs Global argument 


# In[5]:


def greet(name):
    print("Good morning", name)

greet("Alex")


# In[63]:


# Positional Argument:
def power(a,b):
    z= (a**b)
    print(z)
    
power(2,10)


# In[68]:


# Keyward Argument:

def show(name,age):
    print(name,age)
    
show(age=10,name ="dev")


# In[49]:


def show(name,age):
    print(name,age)
    
show(age = 28, name= "dev")


# In[72]:


# Default Argument :
def fun(a=20,b=60,c=80):
    print(a,b,c)

fun()


# In[74]:


# Variable length argument :

def add(x,y):
    z = x+y
    print("addition",z)
add(10,20)


# In[77]:


def Number(*num):
    z = (num[0],num[1],num[2],num[3])
    print("number",z)
Number(10,20,30,50)


# In[78]:


def add(*num):
    z = (num[0]+num[1]+num[2])
    print("addition",z)
add(10,20,30)


# In[80]:


def add(x,*num):
    z = (x+num[0]+num[1]+num[2])
    print(z)

add(1,20,30,40)


# In[50]:


def add(x,*num):
    z = (x+num[0]+num[1])
    print(z)

add(1,20,30,23,54,76,79)


# In[81]:


# local and Global Variable :
 
a = 10

def something():
    a =15
    print("in function",a)

something()

print("out function",a)


# In[82]:


a = 10

def something():
       print("in function",a)

something()


# In[83]:


a = 10

def something():  
        global a
        a =15
        print("in function",a)

something()
print("out function",a)


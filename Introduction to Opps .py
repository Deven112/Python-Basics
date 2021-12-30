#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Introduction to Opps:
    1.Class & Object 
    2.init method 


# In[ ]:


1. Class & Object


# In[3]:


class Student:
    def setdata(self):
        self.name = input ("Enter Name:")
        self.roll = input ("Enter roll:")
        self.per = input ("Enter per:")
    def display(self):
        print("Name",self.name)
        print("roll",self.roll)
        print("per",self.per)

a = Student()
a.setdata()
a.display()


# In[ ]:


2.init method:


# In[4]:


class Student:
    def __init__(self): 
        print("from init")
        self.name = input ("Enter Name:")
        self.roll = input ("Enter roll:")
        self.per = input ("Enter per:")
    def display(self):
        print("Name",self.name)
        print("roll",self.roll)
        print("per",self.per)
a = Student()
a.display()

        
        


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Problem -1
get_ipython().set_next_input('Write a Python function code to calculate the area of the triange on the basis of its base and height');get_ipython().run_line_magic('pinfo', 'height')


# In[38]:


def AreaT (base, height):
    return base * height / 2

AreaT(50,10)
   


# In[ ]:


Problem -2 
Write a Python function to find the Max of three numbers.


# In[35]:


def max_of_two( x, y ):
    if x > y:
        return x
    else:
        return y
max_of_two(10,20)


# In[39]:


def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 10, 8))


# In[ ]:


Problem-3
Write a Python function to sum all the numbers in a set of numbers .


# In[40]:


def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((10,20,30,40)))


# In[ ]:


Problem-4

Write a Python program to print the even numbers from a given list.

Python Even Numbers from 1 to 100


# In[37]:


def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9,12,14,16]))


# In[ ]:


Problem -5 
Write the pyhton function code that will read  a person's name and salary code. The salary code is set of number which 
represents the different salary ammount according to person name. set 1 is the default value of salary code.The salary code 
as follows:
1.- 15000
2.- 20000
3.- 25000
4.- 30000
35.-35000


# In[43]:


def salary(name,scode = 1):
    if scode == 1:
        sal = 15000
    elif scode == 2:
        sal = 20000
    elif scode == 3:
        sal = 25000
    elif scode == 4:
        sal = 30000
    elif scode == 5:
        sal = 35000
    else:
        sal = 15000
    print(name,sal)
    
salary("dev")
    


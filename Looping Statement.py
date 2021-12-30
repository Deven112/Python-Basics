#!/usr/bin/env python
# coding: utf-8

# In[ ]:


l=[10,20,30,40,50,60]

for[userdefined_variable] in [iterable_datatype]:
    [statements]
[outside of the loop]


# In[20]:


l = [10,20,30,40,50]
for value in l:

    print(value)


# In[3]:


s = "pyhton"
for value in s:
    print(value)


# In[30]:


d = {"name":"dev", "contact":12345, "email": "d@gmail.com" }
for x in d:
    print(x)


# In[ ]:


# Adding Elements within the list

l= [10,20,30,40,50]
sum = 0

num1 = 10
sum = 0+10 = 10

num2 = 20
sum = 10+20= 30

num3 = 30
sum = 30+30 = 60

num4 = 40 
sum = 60 + 40 = 100

num5 = 50
sum = 100+50 = 150 


# In[5]:


l= [10,20,30,40,50]
sum = 0

for value in l:
    sum= sum+value
    print(sum)
    
  


# In[ ]:


range(10)      0..........9
range(10,50)   10,11,12..............49
range(10,50,5) 10,15,20,25...........45


# In[ ]:


print(range(10))


# In[38]:


for value in range(5,20,2):
    print(value)


# In[10]:


print(list(range(1,50,5)))


# In[40]:


num1= range(10)
for value in num1:
    print(value)


# In[11]:


s = "python string sample"

vowel_count = 0
consonent_count = 0

for value in s:
    if value in "AEIOUaeiou":
        vowel_count+=1
    else:
        consonent_count+=1
print(vowel_count, consonent_count)


# In[2]:


#While Loop:

#Syntex: while [condition] => true or false
#              [statements ]
    


# In[ ]:


Muitiplying number from 1-5  using while loop


# In[1]:


num1 = 5
result = 1

while num1 > 1:
    result = result*num1
    num1 = num1-1
print(result)
 


# In[2]:


count = 1
sum = 0

while count <= 20:
    sum = sum +count 
    count = count+1
print(sum)


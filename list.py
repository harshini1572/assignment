#!/usr/bin/env python
# coding: utf-8

# In[2]:


List1 = ["python","java"]
List1.append("c++")
print(List1)


# In[4]:


fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()
print(fruits)


# In[5]:


fruits = ['kiwi', 'banana', 'apple', 'orange']

x = fruits.copy()
print(fruits)


# In[9]:


fruits = ['orange', 'apple', 'cherry']

x = fruits.count("cherry")
print(x)


# In[10]:


fruits = ['kiwi', 'banana', 'orange']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)
print(fruits)


# In[11]:


fruits = ['kiwi', 'banana', 'mango']

x = fruits.index("mango")

print(x)


# In[12]:


fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits)


# In[13]:


fruits = ['mango', 'banana', 'orange']

fruits.pop(1)
print(fruits)


# In[14]:


fruits = ['kiwi', 'banana', 'cherry']

fruits.remove("banana")

print(fruits)


# In[15]:


fruits = ['apple', 'mango', 'cherry']

fruits.reverse()

print(fruits)


# In[16]:


cars = ['Ford', 'BMW', 'audi']

cars.sort()

print(cars)


# In[ ]:





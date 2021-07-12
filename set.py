#!/usr/bin/env python
# coding: utf-8

# In[1]:


fruits = {"mango", "banana", "kiwi"}

fruits.add("orange")

print(fruits)


# In[2]:


fruits = {"apple", "banana", "kiwi"}

fruits.clear()

print(fruits)


# In[3]:


fruits = {"apple", "banana", "mango"}

x = fruits.copy()

print(x)


# In[4]:


x = {"apple", "banana", "mango"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)


# In[5]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)


# In[6]:


fruits = {"apple", "banana", "mango"}

fruits.discard("banana")

print(fruits)


# In[8]:


x = {"apple", "banana", "kiwi"}
y = {"google", "microsoft", "banana"}

z = x.intersection(y)

print(z)


# In[9]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)


# In[10]:


x = {"apple", "banana", "kiwi"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)


# In[11]:


x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)


# In[12]:


x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)


# In[14]:


fruits = {"apple", "banana", "orange"}

fruits.pop()

print(fruits)


# In[15]:


fruits = {"apple", "banana", "pineapple"}

fruits.remove("banana")

print(fruits)


# In[16]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)


# In[18]:


x = {"apple", "banana", "kiwi"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)


# In[19]:


x = {"kiwi", "banana", "cherry"}
y = {"google", "microsoft", "kiwi"}

z = x.union(y)

print(z)


# In[20]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)


# In[ ]:





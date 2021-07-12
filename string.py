#!/usr/bin/env python
# coding: utf-8

# In[1]:


txt = "hello this is Harshini."

x = txt.capitalize()

print (x)


# In[2]:


txt = "Hello this is Harshini"

x = txt.casefold()

print(x)


# In[3]:


txt = "Television"

x = txt.center(20)

print(x)


# In[4]:


txt = "an apple a day keeps the doctor away"

x = txt.count("apple")

print(x)


# In[5]:


txt = "My name is harshini"

x = txt.encode()

print(x)


# In[6]:


txt = "Hello This is harshini"

x = txt.endswith(".")

print(x)


# In[7]:


txt = "H\gh\kf\yw\hy"

x =  txt.expandtabs(4)

print(x)


# In[8]:


txt = "Hello this is harshini"

x = txt.find("hello")

print(x)


# In[9]:


txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


# In[11]:


txt = "Hello this is harshini."

x = txt.index("this")

print(x)


# In[12]:


txt = "voice12"

x = txt.isalnum()

print(x)


# In[13]:


txt = "voiceY"

x = txt.isalpha()

print(x)


# In[14]:


txt = "\u0033" #unicode for 3

x = txt.isdecimal()

print(x)


# In[15]:


txt = "65400"

x = txt.isdigit()

print(x)


# In[16]:


txt = "Demo"

x = txt.isidentifier()

print(x)


# In[17]:


txt = "telivision"

x = txt.islower()

print(x)


# In[18]:


txt = "45323"

x = txt.isnumeric()

print(x)


# In[19]:


txt = "Hello! Are you #1?"

x = txt.isprintable()

print(x)


# In[20]:


txt = "   "

x = txt.isspace()

print(x)


# In[21]:


txt = "welcome to india"

x = txt.istitle()

print(x)


# In[22]:


txt = "THIS IS NOW!"

x = txt.isupper()

print(x)


# In[23]:


myTuple = ("sunny", "George", "brownie")

x = "#".join(myTuple)

print(x)


# In[24]:


txt = "pear"

x = txt.ljust(20)

print(x, "is my favorite fruit.")


# In[25]:


txt = "Hello THIS is HARSHINI"

x = txt.lower()

print(x)


# In[26]:


txt = "     apple    "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")


# In[28]:


txt = "Hello yaak!"
mytable = txt.maketrans("y", "P")
print(txt.translate(mytable))


# In[29]:


txt = "I could eat kiwis all day"

x = txt.partition("kiwis")

print(x)


# In[30]:


txt = "I like oranges"

x = txt.replace("oranges", "pineapples")

print(x)


# In[31]:


txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)


# In[32]:


txt = "shi tzu, ku tzu."

x = txt.rindex("tzu")

print(x)


# In[33]:


txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")


# In[34]:


txt = "banana"

x = txt.rjust(20, "O")

print(x)


# In[35]:


txt = "I could eat kiwis all day, kiwis are my favorite fruit"

x = txt.rpartition("kiwis")

print(x)


# In[36]:


txt = "kiwi,orange,apple"

x = txt.rsplit(", ")

print(x)


# In[37]:


txt = "welcome to my home"

x = txt.split()

print(x)


# In[38]:


txt = "i am happy \nWelcome to my home"

x = txt.splitlines()

print(x)


# In[39]:


txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)


# In[40]:


txt = "Hello, welcome to my world."

x = txt.startswith("wel", 7, 20)

print(x)


# In[42]:


txt = "     kiwi   "

x = txt.strip()

print("of all fruits", x, "is my favorite")


# In[43]:


txt = "Hello My Name Is Harshini"

x = txt.swapcase()

print(x)


# In[44]:


txt = "Welcome to home"

x = txt.title()

print(x)


# In[46]:


txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))


# In[47]:


txt = "Hello This is harshini"

x = txt.upper()

print(x)


# In[48]:


txt = "50"

x = txt.zfill(10)

print(x)


# In[ ]:





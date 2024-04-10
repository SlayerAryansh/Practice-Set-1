#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#3) Create a function, that determine whether it is a leap year. If it is a leap year, return theBoolean True, otherwise return False.


# In[9]:


def leap_year():
    year = int(input("No. "))
    if (year % 4 == 0):
        return True
    else:
        return False
leap_year()


# In[ ]:





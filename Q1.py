#!/usr/bin/env python
# coding: utf-8

# In[18]:


#Given an integer, n, perform the following conditional actions:
#If n is odd, print weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of 6 to 20, print Weird
#If n is even and greater than 20, print Not Weird


# In[25]:


n = int(input("No. "))
if n % 2 != 0:
    print("Weird")
else:
    if 2<= n <= 5:
        print("Not weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
            print("Not weird")
        


# n = int(input("No. "))

# In[ ]:


n = int(input("No. "))
for 


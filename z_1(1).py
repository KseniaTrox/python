#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[36]:


x = np.linspace(0, 10, 80)
plt.title('Lesson 4')
plt.grid()
plt.xlabel('x', color='red', fontsize=14)
plt.ylabel('y', color='red', fontsize=14)
k = 1
k1 = 2
plt.plot(x,np.cos(k*x), 'ro', label='k')
plt.plot(x,np.cos(k1*x), label='k1')
plt.legend()


# In[ ]:





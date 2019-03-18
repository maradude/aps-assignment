#!/usr/bin/env python
# coding: utf-8

from IPython import get_ipython

# # Benchmarking 1d range search

# In[1]:


import Task11
import Task12
import Task21
from sanitize_input import Tests
import random


# In[46]:


log10 = [random.randrange(1, 1000, 1) for n in range(10)]
log100 = [random.randrange(1, 1000, 1) for n in range(100)]
log1_000 = [random.randrange(1, 1000, 1) for n in range(1_000)]
log10_000 = [random.randrange(1, 1000, 1) for n in range(10_000)]
log100_000 = [random.randrange(1, 1000, 1) for n in range(100_000)]
log1_000_000 = [random.randrange(1, 1000, 1) for n in range(1_000_000)]


# In[ ]:


lbound, ubound = 250, 600


# ## Naïve

# In[4]:


get_ipython().run_line_magic('timeit', 'Task11.get_range(log10, lbound, ubound)')


# In[5]:


get_ipython().run_line_magic('timeit', 'Task11.get_range(log100, lbound, ubound)')


# In[6]:


get_ipython().run_line_magic('timeit', 'Task11.get_range(log1_000, lbound, ubound)')


# In[7]:


get_ipython().run_line_magic('timeit', 'Task11.get_range(log10_000, lbound, ubound)')


# In[8]:


get_ipython().run_line_magic('timeit', 'Task11.get_range(log100_000, lbound, ubound)')


# In[9]:


get_ipython().run_line_magic('timeit', 'Task11.get_range(log1_000_000, lbound, ubound)')


# Above is the naïve implementation times, as you can see it looks like a constant operation from ten to a million

# ## Binary search, build + search

# In[10]:


get_ipython().run_line_magic('timeit', 'Task12.SortedRangeList(log10).get_range(lbound, ubound)')


# In[11]:


get_ipython().run_line_magic('timeit', 'Task12.SortedRangeList(log100).get_range(lbound, ubound)')


# In[12]:


get_ipython().run_line_magic('timeit', 'Task12.SortedRangeList(log1_000).get_range(lbound, ubound)')


# In[13]:


get_ipython().run_line_magic('timeit', 'Task12.SortedRangeList(log10_000).get_range(lbound, ubound)')


# In[14]:


get_ipython().run_line_magic('timeit', 'Task12.SortedRangeList(log100_000).get_range(lbound, ubound)')


# In[15]:


get_ipython().run_line_magic('timeit', 'Task12.SortedRangeList(log1_000_000).get_range(lbound, ubound)')


# above is the binary search implementation times, as you can see it looks linear from ten to a million

# ## Rangetree, build + search

# In[16]:


get_ipython().run_line_magic('timeit', 'Task21.RangeTree(log10).one_d_range_query(lbound, ubound)')


# In[17]:


get_ipython().run_line_magic('timeit', 'Task21.RangeTree(log100).one_d_range_query(lbound, ubound)')


# In[18]:


get_ipython().run_line_magic('timeit', 'Task21.RangeTree(log1_000).one_d_range_query(lbound, ubound)')


# In[19]:


get_ipython().run_line_magic('timeit', 'Task21.RangeTree(log10_000).one_d_range_query(lbound, ubound)')


# In[20]:


get_ipython().run_line_magic('timeit', 'Task21.RangeTree(log100_000).one_d_range_query(lbound, ubound)')


# In[21]:


get_ipython().run_line_magic('timeit', 'Task21.RangeTree(log1_000_000).one_d_range_query(lbound, ubound)')


# ## Time to build RangeTee

# In[22]:


get_ipython().run_line_magic('timeit', 'Task21.RangeTree(log10)')


# In[23]:


get_ipython().run_line_magic('timeit', 'Task21.RangeTree(log100)')


# In[24]:


get_ipython().run_line_magic('timeit', 'Task21.RangeTree(log1_000)')


# In[25]:


get_ipython().run_line_magic('timeit', 'Task21.RangeTree(log10_000)')


# In[26]:


get_ipython().run_line_magic('timeit', 'Task21.RangeTree(log100_000)')


# In[27]:


get_ipython().run_line_magic('timeit', 'Task21.RangeTree(log1_000_000)')


# ## Time to build sorted range list (i.e. timsort)

# In[28]:


get_ipython().run_line_magic('timeit', 'Task12.SortedRangeList(log10)')


# In[29]:


get_ipython().run_line_magic('timeit', 'Task12.SortedRangeList(log100)')


# In[30]:


get_ipython().run_line_magic('timeit', 'Task12.SortedRangeList(log1_000)')


# In[31]:


get_ipython().run_line_magic('timeit', 'Task12.SortedRangeList(log10_000)')


# In[32]:


get_ipython().run_line_magic('timeit', 'Task12.SortedRangeList(log100_000)')


# In[33]:


get_ipython().run_line_magic('timeit', 'Task12.SortedRangeList(log1_000_000)')


# ## Rangtree pre built tree search

# In[ ]:


a = Task21.RangeTree(log10)
b = Task21.RangeTree(log100)
c = Task21.RangeTree(log1_000)
d = Task21.RangeTree(log10_000)
e = Task21.RangeTree(log100_000)
f = Task21.RangeTree(log1_000_000)


# In[34]:


get_ipython().run_line_magic('timeit', 'a.one_d_range_query(lbound, ubound)')


# In[35]:


get_ipython().run_line_magic('timeit', 'b.one_d_range_query(lbound, ubound)')


# In[36]:


get_ipython().run_line_magic('timeit', 'c.one_d_range_query(lbound, ubound)')


# In[37]:


get_ipython().run_line_magic('timeit', 'd.one_d_range_query(lbound, ubound)')


# In[38]:


get_ipython().run_line_magic('timeit', 'e.one_d_range_query(lbound, ubound)')


# In[39]:


get_ipython().run_line_magic('timeit', 'f.one_d_range_query(lbound, ubound)')


# ## Binary search, presorted search

# In[ ]:


i = Task12.SortedRangeList(log10)
ii = Task12.SortedRangeList(log100)
iii = Task12.SortedRangeList(log1_000)
iv = Task12.SortedRangeList(log10_000)
v = Task12.SortedRangeList(log100_000)
vi = Task12.SortedRangeList(log1_000_000)


# In[40]:


get_ipython().run_line_magic('timeit', 'i.get_range(lbound, ubound)')


# In[41]:


get_ipython().run_line_magic('timeit', 'ii.get_range(lbound, ubound)')


# In[42]:


get_ipython().run_line_magic('timeit', 'iii.get_range(lbound, ubound)')


# In[43]:


get_ipython().run_line_magic('timeit', 'iv.get_range(lbound, ubound)')


# In[44]:


get_ipython().run_line_magic('timeit', 'v.get_range(lbound, ubound)')


# In[45]:


get_ipython().run_line_magic('timeit', 'vi.get_range(lbound, ubound)')


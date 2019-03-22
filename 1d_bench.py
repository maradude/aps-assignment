#!/usr/bin/env python
# coding: utf-8

# # Benchmarking 1d range search

# In[3]:


import Task11
import Task12
import Task21
from sanitize_input import Tests
import random
import numpy as np
import matplotlib.pyplot as plt
from itertools import count


# In[4]:


# log10 = [random.randrange(1, 1000, 1) for n in range(10)]
# log100 = [random.randrange(1, 1000, 1) for n in range(100)]
# log1_000 = [random.randrange(1, 1000, 1) for n in range(1_000)]
# log10_000 = [random.randrange(1, 1000, 1) for n in range(10_000)]
# log100_000 = [random.randrange(1, 1000, 1) for n in range(100_000)]
# log1_000_000 = [random.randrange(1, 1000, 1) for n in range(1_000_000)]
# n_sizes = [log10, log100, log1_000, log10_000, log100_000, log1_000_000] 


# In[5]:


# lo, hi = 250, 600


# In[6]:


def random_bound1d():
    a = random.randrange(1, 999, 1)
    return a, random.randrange(a, 1000, 1)


# In[7]:


random_bound1d()


# In[ ]:





# In[8]:


bounds = (random_bound1d() for _ in count())


# In[9]:


print(*next(bounds))


# In[10]:


def naive_bench(elements, *_):
    bounds = [random_bound1d() for _ in range(100)]
    res = []
    for n in elements:
        bres = []
        b = len(n)
        print(f'---{b}---')
        for l, u in bounds:
            a = get_ipython().run_line_magic('timeit', '-o -r1 list(Task11.get_range(n, l, u))')
            bres.append(a)
        res.append((b,bres))
    return res


# ## Naïve

# In[ ]:


naive_bench(n_sizes)


# Above is the naïve implementation times, as you can see it looks like a constant operation from ten to a million

# ## Binary search, build + search

# In[11]:


def b_search_with_build(elements, lo, hi):
    res = []
    for n in elements:
        b = len(n)
        a = get_ipython().run_line_magic('timeit', '-o -r1 Task12.SortedRangeList(n).get_range(lo, hi)')
        res.append((b,a))
    return res


# In[114]:


b_search_with_build(n_sizes, lbound, ubound)


# ## Rangetree, build + search

# In[12]:


def tree_search_with_build(elements, lo, hi):
    res = []
    for n in elements:
        b = len(n)
        a = get_ipython().run_line_magic('timeit', '-o -r1 Task21.RangeTree(n).one_d_range_query(lo, hi)')
        res.append((b,a))
    return res


# In[120]:


tree_search_with_build(n_sizes, lbound, ubound)


# ## Time to build RangeTee 

# In[13]:


def build_range_tree(elements, *_):
    res = []
    for n in elements:
        resb = []
        b = len(n)
        print(f'---{b}---')
        for n in range(100):
            m = [random.randrange(1, 1000, 1) for _ in range(b)]
            a = get_ipython().run_line_magic('timeit', '-o -r1 Task21.RangeTree(m)')
            resb.append(a)
        res.append((b,resb))
    return res


# In[ ]:


build_range_tree(n_sizes)


# ## Time to build sorted range list (i.e. timsort)

# In[14]:


def build_sorted_list(elements, *_):
    res = []
    for n in elements:
        resb = []
        b = len(n)
        print(f'---{b}---')
        for i in range(100):
            m = [random.randrange(1, 1000, 1) for _ in range(b)]
            a = get_ipython().run_line_magic('timeit', '-o -r1 Task12.SortedRangeList(m)')
            resb.append(a)
        res.append((b,resb))
    return res


# In[ ]:


build_sorted_list(n_sizes)


# ## Rangtree pre built tree search

# In[15]:


"""
def build_range_tree(elements, *_):
    res = []
    for n in elements:
        resb = []
        m = n.copy()
        b = len(n)
        for n in range(10):
            random.shuffle(m)
            a = %timeit -o Task21.RangeTree(m)
            resb.append(a)
        print(f'^{len(n)}^')
        res.append((b,resb))
    return res
    
    def naive_bench(elements, lo, hi):
    bounds = [random_bound1d() for _ in range(10)]
    res = []
    for n in elements:
        bres = []
        for l, u in bounds:
            b = len(n) 
            a = %timeit -o list(Task11.get_range(n, l, u))
            bres.append(a)
        print(f'^ {len(n)} ^')
        res.append((b,bres))
    return res
    
"""
def tree_search_only(elements, *_):
    objs = (Task21.RangeTree(e) for e in elements)
    bounds = [random_bound1d() for _ in range(100)]
    res = []
    for i, n in enumerate(objs):
        bres  = []
        b = 10**(i+1)
        print(f'---{b}---')
        for l, h in bounds: 
            a = get_ipython().run_line_magic('timeit', '-o -r1 n.one_d_range_query(l, h)')
            bres.append(a)
        res.append((b,bres))
    return res


# In[ ]:


tree_search_only(n_sizes)


# ## Binary search, presorted search

# In[16]:


def b_search_only(elements, *_):
    objs = (Task12.SortedRangeList(e) for e in elements)
    bounds = [random_bound1d() for _ in range(100)]
    res = []
    for i, n in enumerate(objs):
        bres  = []
        b = 10**(i+1)
        print(f'---{b}---')
        for l, h in bounds: 
#            print(l, h)
            a = get_ipython().run_line_magic('timeit', '-o -r1 n.get_range(l, h)')
            bres.append(a)
        res.append((b,bres))
    return res


# In[8]:


b_search_only(n_sizes)


# In[17]:


def print_thing(r):
    return [(i, m.average, m.stdev) for i, m in r]


# In[18]:


def try_bounds(es):
    funcs = [naive_bench, # b_search_with_build, tree_search_with_build,
             build_range_tree, build_sorted_list, tree_search_only,
             b_search_only]
    return [(r.__name__, r(es)) for r in funcs if not print(r.__name__)]


# In[22]:


dis = try_bounds(n_sizes)


# In[ ]:


dis_new = try_bounds(n_sizes)


# In[40]:


import pickle
pickle.dump( dis, open( "save.p", "wb" ) )


# In[23]:


dis


# In[30]:




with open('results.txt', 'w') as f:
    af = '\n'.join(str(e) for e in dis)
    f.write(af)


# In[13]:


try_bounds(n_sizes, 0, 100)


# In[211]:


m


# In[212]:


m.all_runs


# In[216]:


m.average * m.loops


# In[218]:


sum(m.all_runs)/len(m.all_runs)


# In[237]:


log10


# ## plot plan
# Plan is probably to display the data from a np dataframe to matplotlib. The plot will probably be line graphs with ranges such as: precise (within 20%), with all on 1 side of median and not, broad (80%), middle (50%) and 1 element query. 

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[308]:


# naive_bench, b_search_with_build, tree_search_with_build, build_range_tree, build_sorted_list, tree_search_only, b_search_only
names = ["Bruteforce", "Binary search + build", "Tree search + build", "Build Tree", "Sort Array", "Tree search", "Binary search"]


# In[309]:


fig, ax = plt.subplots()
le = len(n_sizes)
for p,i in enumerate(dis):
    a = [str(10**i) for i in range(1,7)]
    plt.yscale('log')
    err = np.array([e[2] for e in i[1]])
    v = np.array([e[1] for e in i[1]])
    print(v,'woot', err)
    ax.errorbar(a, v, err, fmt='-|', elinewidth=10, barsabove=1, label=names[p])
    ax.legend()
    
ax.set_xlabel("Amount of points")
ax.set_ylabel("Seconds (log scale)")
ax.set_title("Time taken for a single 1d range search")
#plt.axis([10, int(1e6), 0, 4])


# In[310]:


#plt.tight_layout()
#format_axes(ax)
fig.savefig("250-600_plot.png")


# In[181]:


dis[0][1]


# In[229]:


#import pandas as pd
import matplotlib
from math import sqrt
SPINE_COLOR = 'gray'


# In[281]:


def latexify(fig_width=None, fig_height=None, columns=1):
    """Set up matplotlib's RC params for LaTeX plotting.
    Call this before plotting a figure.

    Parameters
    ----------
    fig_width : float, optional, inches
    fig_height : float,  optional, inches
    columns : {1, 2}
    """

    # code adapted from http://www.scipy.org/Cookbook/Matplotlib/LaTeX_Examples

    # Width and max height in inches for IEEE journals taken from
    # computer.org/cms/Computer.org/Journal%20templates/transactions_art_guide.pdf

    assert(columns in [1,2])

    if fig_width is None:
        fig_width = 3.39 if columns==1 else 6.9 # width in inches

    if fig_height is None:
        golden_mean = (sqrt(5)-1.0)/2.0    # Aesthetic ratio
        fig_height = fig_width*golden_mean # height in inches

    MAX_HEIGHT_INCHES = 8.0
    if fig_height > MAX_HEIGHT_INCHES:
        print("WARNING: fig_height too large:" + fig_height + 
              "so will reduce to" + MAX_HEIGHT_INCHES + "inches.")
        fig_height = MAX_HEIGHT_INCHES

    params = {'backend': 'ps',
              'text.latex.preamble': ['\\usepackage{gensymb}'],
              'axes.labelsize': 14, # fontsize for x and y labels (was 10)
              'axes.titlesize': 14,
#              'text.fontsize': 10, # was 10
              'legend.fontsize': 14, # was 10
              'xtick.labelsize': 14,
              'ytick.labelsize': 14,
              'text.usetex': True,
              'figure.figsize': [fig_width,fig_height],
              'font.family': 'serif'
    }

    matplotlib.rcParams.update(params)


def format_axes(ax):

    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

    for spine in ['left', 'bottom']:
        ax.spines[spine].set_color(SPINE_COLOR)
        ax.spines[spine].set_linewidth(0.5)

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_tick_params(direction='out', color=SPINE_COLOR)

    return ax


# In[282]:


width = 12.9
format_axes(ax)
latexify(width, width*(sqrt(5)-1.0)/2.0 )


# In[19]:


dis_new = try_bounds(n_sizes)


# In[ ]:


import pickle
pickle.dump(dis_new, open("1d.p", "wb"))


# In[ ]:





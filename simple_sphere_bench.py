#!/usr/bin/env python
# coding: utf-8


import Task43
import Task51
import Task53
from sanitize_input import Tests
import random
import numpy as np
import matplotlib.pyplot as plt
from itertools import count



def random_coords(n,d):
    return [[random.randrange(1, 1000, 1) for _ in range(d)] for _ in range(n)]


d2n10 = random_coords(10, 2)
d2n100 = random_coords(100, 2)
d2n1_000 = random_coords(1000, 2)
d2n10_000 = random_coords(10_000, 2)
d2n100_000 = random_coords(100_000, 2)
d2n1_000_000 = random_coords(1_000_000, 2)
n_sizes = [d2n10, d2n100, d2n1_000, d2n10_000, d2n100_000, d2n1_000_000]


def create_test_ns(d):
    return [random_coords(10**i, d) for i in range(1,7)]


def random_boundkd(d):
    a = random_coords(1, d)[0]
    b = random.randrange(0, 500, 1)
    return a, b


# In[9]:


random_boundkd(5)


def sphere_query(e, *_, d=2, c=100):
    res = []
    bounds = [random_boundkd(d) for _ in range(c)]
    for n in e:
        bres = []
        d = len(n)
        a = Task43.KDTree(n).root
        print(f'---{d}---')
        for l, u in bounds:
            b = list(zip(l, u))
            c = get_ipython().run_line_magic('timeit', '-o -r1 Task55.sphere_query(a, b)')
            bres.append(c)
        res.append((d, c))
    return res


def print_thing(r, nam):
    print(nam)
    return [(i, m.average, m.stdev) for i, m in r]


# In[43]:


def try_bounds2():
    res = []
    # funcs = [bruteforce, build_kd_tree, kd_tree_without_contained, kd_tree_with_contained]
    funcs = [sphere_query]
    ds= [2,3,5,10,50]
    es = (random_coords(1_000_000, d) for d in ds)
    for d, e in zip(ds, es):
        print(d,len(e))
        bres = []
        print(d)
        for f in funcs:
            print(f.__name__)
            bres.append((f.__name__, f([e], d=d)))
        res.append(bres)
    return res


# In[26]:


def try_bounds(es, d=2):
    # funcs = [bruteforce, build_kd_tree, kd_tree_without_contained, kd_tree_with_contained]
    funcs = [sphere_query]
    return [(f.__name__, f(create_test_ns(2), d=d)) for f in funcs if not print(f.__name__)]


# In[ ]:


try_bounds(create_test_ns(2))


# In[44]:


try_bounds2()


# In[36]:


dis2 = try_bounds(n_sizes, 250, 600, 2)
dis2


# In[ ]:


dis


# In[ ]:


dis10 = try_bounds(create_test_ns(10), 250, 600, 10)


# In[ ]:


dis10


# In[41]:


dis50 = try_bounds(create_test_ns(50), 250, 600, 50)
dis50


# In[34]:


def generate_dimension(lbound, ubound, ds):
    return [([lbound]*e, [ubound]*e) for e in ds]


# In[2]:


def try_bounds2(lo, up):
    a = [1,2,3,5,10,50]
    d = generate_dimension(lo, up, a)
    print(d[0])
    es = [random_coords(1000, i) for i in a]
    funcs = [bruteforce, build_kd_tree, kd_tree_without_contained, kd_tree_with_contained]
#         kd_tree_without_contained_plus_build, kd_tree_with_contained_plus_build]
    res = []
    for l,u in d:
        for f in funcs:
            print(f.__name__)
            res.append((f.__name__, f(es, l, u), f.__name__))
    return res


# In[36]:


disn = try_bounds2(250, 600)


# In[ ]:


with open('results.txt', 'w') as f:
    af = '\n'.join(str(e) for e in dis)
    f.write(af)


# ## plot plan
# Plan is probably to display the data from a np dataframe to matplotlib. The plot will probably be line graphs with ranges such as: precise (within 20%), with all on 1 side of median and not, broad (80%), middle (50%) and 1 element query.

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


names = ["Bruteforce", "Build KD-tree", "KD-tree only intersection", "KD-tree with contained"]
#         "KD-tree build + intersection only search", "KD-tree build + with contained search"]


# In[32]:


def draw_plot(n, data, title):
    fig, ax = plt.subplots()
    a = [str(10**i) for i in range(1,n)]
    for p,i in enumerate(data):
        plt.yscale('log')
        err = np.array([e[2] for e in i[1]])
        v = np.array([e[1] for e in i[1]])
#        print(err,'WOOT', v)
#        print(a, v, err)
        ax.errorbar(a, v, err, fmt='-|', elinewidth=10, barsabove=1, label=names[p])
    ax.legend()
    ax.set_xlabel("Amount of points")
    ax.set_ylabel("Seconds (log scale)")
    ax.set_title(title)
    #width = 12.9
    #format_axes(ax)
    #latexify(width, width*(sqrt(5)-1.0)/2.0 )
    fig.savefig(f"{title}.png")
    plt.show()
#draw_plot(7, dis, "Time taken for a single 2d range search")


# In[38]:


draw_plot(7, dis2, "Time taken for a single 2d range search")


# In[ ]:


draw_plot(7, dis10, "Time taken for a single 10d range search")


# In[ ]:


draw_plot(7, dis100, "Time taken for a single 100d range search")


# In[42]:


draw_plot(7, dis50, "Time taken for a single 50d range search")


# In[ ]:


draw_plot(7, dis10, "Time taken for a single 10d range search")


# In[ ]:


#plt.tight_layout()
#format_axes(ax)
#fig.savefig("250-600_plot.png")


# In[ ]:


dis[0][1]


# In[ ]:


#import pandas as pd
import matplotlib
from math import sqrt
SPINE_COLOR = 'gray'


# In[ ]:


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


# In[45]:


import pickle


# In[ ]:


var_ele = try_bounds(create_test_ns(2))


# In[ ]:


var_dim = try_bounds2()


# In[46]:


import pickle
pickle.dump( var_ele, open( "variable_elements.p", "wb" ) )
pickle.dump( var_dim, open( "variable_dimensions.p", "wb"))


# In[ ]:





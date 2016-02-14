
# coding: utf-8

# # Integral Evaluation with Monte Carlo Methods

# This program uses Monte Carlo to estimate the integrals of the following: x, x^2, and sin(pi*x). The upper and lower bounds for these functions will be 1 and 0, respectively. 

# In[1]:

import numpy as np
np.random.seed(seed=27) # to obtain reproducible results

N = 1000000 # number of samples
x = np.random.rand(N) # sample x values uniformly
# apply functions
f_1 = x
f_2 = x**2
f_3 = np.sin(x*np.pi)
# sum results ( calculate integrals )
int_1 = np.sum(f_1)/N
int_2 = np.sum(f_2)/N
int_3 = np.sum(f_3)/N
# estimate errors
err_1 = np.std(f_1)/np.sqrt(N)
err_2 = np.std(f_2)/np.sqrt(N)
err_3 = np.std(f_3)/np.sqrt(N)


print "integral - f(x) = x - [0,1]         :"       "{:.5f} \pm {:.5f}".format(int_1, err_1)
print "integral - f(x) = x**2 - [0,1]      :"       "{:.5f} \pm {:.5f}".format(int_2, err_2)
print "integral - f(x) = sin(x*pi) - [0,1] :"       "{:.5f} \pm {:.5f}".format(int_3, err_3)


# In[ ]:




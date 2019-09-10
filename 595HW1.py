# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:47:23 2019

@author: bhaku
"""

import matplotlib.pyplot as plt
import numpy as np
#number_of_pi=8
def sincosplot(number_of_pi=2,increment=0.1):
    x = np.arange(0,number_of_pi*np.pi,increment)   # start,stop,step
    y = np.sin(x)   
    z = np.cos(x)
    plt.plot(x,y,x,z)
    plt.show()
sincosplot()

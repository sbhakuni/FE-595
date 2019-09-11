# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:47:23 2019

@author: bhaku
"""

import matplotlib.pyplot as plt
import numpy as np

def sincosplot(number_of_pi=2,increment=0.1):
    x = np.arange(0,number_of_pi*np.pi,increment)
    y = np.sin(x)   
    z = np.cos(x)
    plt.plot(x,y,x,z,)
    plt.plot(x,y,x,z)
    plt.xlabel('x values for one period') 
    plt.ylabel('sin(x) and cos(x)')
    plt.title('Plot of sin(x) and cos(x) for one period(0 to 2pi)')
    plt.legend(['sin(x)', 'cos(x)'])  
    plt.show()

sincosplot()

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 11:39:22 2017

@author: hp
"""


import math
from math import exp , sqrt , log
from sys import exit , stderr
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.stats import norm


M = 10000

m_array=[7,11,14]

N=list(range(3))



for i in range(3):
    N[i]=2*m_array[i]
    n=N[i]
    Pf_ad = [0.001,0.0029,0.005,0.0062,0.0078,0.01,0.0154,0.025,0.0346,0.05,0.0632,0.081,0.1,0.1186,0.15,0.2027,0.2676,0.3573,0.4142,0.4463,0.481,0.5185,0.5588,0.5801,0.607,0.6247,0.648,0.7468,0.8487,0.9382,0.9904,0.9997]; 
    snr_avgdB = -2; 
    snr_avg = pow(10,snr_avgdB/10);
    Pd_sim_ad=list(range(len(Pf_ad)))
    AD_test=list(range(len(Pf_ad)))
    for j in range(len(Pf_ad)):
        des=0
        c_value_ad = [6.000,5,4.500,4.3,4.1,3.857,3.5,3.070,2.8,2.4920,2.3,2.1,1.933,1.8,1.610,1.4,1.2,1,0.9,0.850,0.8,0.75,0.7,0.675,0.650,0.625,0.6,0.5,0.4,0.3,0.2,0.125]; 
        for kk in list(range(M)):
            m=1
            noise=np.random.randn(1,N[i])
            q=math.sqrt(snr_avg)
            x = np.add(q,noise)
            x=x[:]
            x=np.sort(x)
            fx=norm(0,1).cdf(x)
            print(fx)
            e=[w for w in range(1,n+1)]
            temp_fx=fx[0:n]
            S=np.sum(np.multiply(np.subtract(np.multiply(2,e),1),np.add(np.log(temp_fx),np.log(np.subtract(1,temp_fx[:,::-1])))))
            #print(S)
            AD_test[j] = -n-(S/n)
            print(AD_test[j])
            if AD_test[j] >= c_value_ad[j]:
                des = des + 1
                
        Pd_sim_ad[j] = des/M
    #print(S)
    #print(AD_test)
    #print(Pd_sim_ad)
    plt.plot(Pf_ad,Pd_sim_ad)
    plt.xlabel('False Alarm')
    plt.ylabel('Probability of Detection')
    plt.savefig('AD_ROC.PNG')

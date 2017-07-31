# -*- coding: utf-8 -*-
"""
@author: Jay
"""
import math
from math import exp , sqrt , log
from sys import exit , stderr
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


M=20000
N=30
Pf=0.01
SNR=list(range(11))
for i in range(11):
    SNR[i]=(-1)*(i)
print(SNR)


snr_avg=np.power(10,np.divide(SNR,10))
q=np.sqrt(snr_avg)
print(q)

Pd_Sim=list(range(len(q)))
for i in range(len(q)):
    des=0
    threshold=2*sp.special.gammainccinv(N,Pf)
    print(threshold)
    for kk in list(range(M)):
        x=np.random.randn(1,N)+1j*np.random.randn(1,N)
        noise=np.random.randn(1,N)+1j*np.random.randn(1,N)
        y=x*q[i]+noise
        
        Test_Stats=np.sum(abs(y**2))
        #print(Test_Stats)
        if Test_Stats>threshold:
            des+=1
    Pd_Sim[i]=des/M
    
print(Pd_Sim)
plt.plot(SNR,Pd_Sim)
plt.xlabel('SNR')
plt.ylabel('Probability of Detection')
plt.show()

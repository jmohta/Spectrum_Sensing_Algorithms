#Libraries of python that are used
import math
from math import exp , sqrt , log
from sys import exit , stderr
import numpy as np
import scipy as sp
from scipy import special
import matplotlib.pyplot as plt


#Logic starts from here
M=10000                 #M variable taken for Monte Carlo Simulation
N=20                #N is the number of samples
Pf=list(range(101))     #A list for Storing Probability of false alarm is taken
for i in range(101):        #This loop stores the value of false alarm probability from 0.01 to 1 with spacing of 0.01
    Pf[i]=(i)/100
print(Pf)               #Prints the list of false alarm probabilities

snr_avgdB=[-4,2]                            #Two values of SNR is taken for comparison
snr_avg=np.power(10,np.divide(snr_avgdB,10))        #Average of SNR is calculated by the formula
q=np.sqrt(snr_avg)                      #A variable q stores the value of square root of SNR
print(q)



threshold=list(range(len(Pf)))                  #A list is defined to store the different values of threshold
Test_Stats=list(range(len(Pf)))                 #An another list is defined to store the test statistics
w, h = len(Pf), len(q);
Pd_Sim = [[0 for x in range(w)] for y in range(h)] 
for j in range(len(q)):
    for i in range(len(Pf)):
        des=0
        threshold[i]=2*sp.special.gammainccinv(N,Pf[i])             #This formula calculates the threshold 
        print(threshold[i])
        for kk in list(range(M)):                               #Monte Carlo loop starts from here
            x=np.random.randn(1,N)+1j*np.random.randn(1,N)              #A random signal is generated
            noise=np.random.randn(1,N)+1j*np.random.randn(1,N)          #A quassian noise is also generated
            y=x*q[j]+noise                                          #The model is created by adding signal and noise
            Test_Stats[i]=np.sum(abs(y**2)) 
            if Test_Stats[i]>threshold[i]:                      #The test statistics and threshold is compared to see whether signal is present or not
                des+=1                                      #The desicion value is incremented
        Pd_Sim[j][i]=des/M
    
#Pd_Sim[0][:]=Pd_Sim[0][::-1]
#Pd_Sim[1][:]=Pd_Sim[1][::-1]
#print(Pd_Sim[1][:])
plt.xticks(np.arange(min(Pf), max(Pf), 0.1))                
plt.yticks(np.arange(0, 1, 0.1))
plt.plot(Pf,Pd_Sim[0],Pf,Pd_Sim[1])         #Both graphs are ploted using library in python
plt.xlabel('False Alarm')                   #X-axis is labelled as False alarm
plt.ylabel('Probability of Detection')      #Y-axis is labelled as Probability of Detection
plt.show()                                  #This command shows the graph

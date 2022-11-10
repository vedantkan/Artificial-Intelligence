#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def filtering(evidence_data_add, prior, total_day):
    # you need to implement this method.

    x_prob_rain = []
    rain_prob = []
    p = np.array([[prior[0]],[prior[1]]])    # create an array to store the prior values
    prior = p
    f = open(evidence_data_add, "r")
    
    for line in f:
        sensor = 'take' in line         
        rain = np.array([[0.7, 0.3], [0.3, 0.7]])   # create a transition model values array        
        if sensor:  # if loop for when the director has taken the umbrella        
            p_val = np.array([[0.9, 0.0], [0.0, 0.2]])  # create a sensor model values array for when the umbrella was taken            
            a = np.matmul(p_val, rain)   # matrix multiplication to get P(U|R)P(R1|R0)            
            temp = np.matmul(a, prior)   # matrix multiplication with alpha             
            tempsum = temp[0] + temp[1]  # calculate the new value of alpha
            temp[0] = temp[0] / tempsum
            temp[1] = temp[1] / tempsum
            prior = temp
        
        else:  # create a sensor model values array when the umbrella was not taken
            n_val = np.array([[0.1,0.0],[0.0,0.8]])  # create a sensor model values array for when the umbrella was not taken            
            a = np.matmul(n_val, rain)  # matrix multiplication to get P(U|R)P(R1|R0)             
            temp = np.matmul(a, prior)  # matrix multiplication with alpha            
            tempsum = temp[0] + temp[1] # calculate the new value of alpha
            temp[0] = temp[0] / tempsum
            temp[1] = temp[1] / tempsum
            prior = temp             
        
        rain_prob.append(prior)
        
    for i in range(100):        
        x_prob_rain.append(rain_prob[i][0])
        
    return x_prob_rain

# following lines are main function:
evidence_data_add = "assign2_umbrella.txt"
total_day = 100
# the prior distribution on the initial state, P(X0). 50% rainy, and 50% sunny on day 0.
prior = [0.5, 0.5]

x_prob_rain=filtering(evidence_data_add, prior, total_day)
for i in range(100):
    print("Day " + str(i+1) + ": rain " + str(x_prob_rain[i]) + ", sunny " + str(1 - x_prob_rain[i]))


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd

def prediction(evidence_data_add, prior, start_day, end_day):
    prob_rain = []
    rain_prob = []
    x_prob_rain = []
    p = np.array([[prior[0]],[prior[1]]])
    prior = p
    
    f = open(evidence_data_add, "r")      # we first perform filtering to get prob of rain from day 1 to day 100
    for line in f:
        sensor = 'take' in line
        rain = np.array([[0.7, 0.3], [0.3, 0.7]])
        if sensor:
            p_val = np.array([[0.9, 0.0], [0.0, 0.2]])
            a = np.matmul(p_val, rain)
            temp = np.matmul(a, prior)
            tempsum = temp[0] + temp[1]
            temp[0] = temp[0] / tempsum
            temp[1] = temp[1] / tempsum
            prior = temp

        else:
            n_val = np.array([[0.1,0.0],[0.0,0.8]])
            a = np.matmul(n_val, rain)
            temp = np.matmul(a, prior)
            tempsum = temp[0] + temp[1]
            temp[0] = temp[0] / tempsum
            temp[1] = temp[1] / tempsum
            prior = temp             
        
        rain_prob.append(prior)
        
    for i in range(0, 100):
        prob_rain.append(rain_prob[i][0])    # end of filtering
    
    
    last_val = prob_rain[99]   # we store the probabilities of day 100 into a variable

    for i in range(start_day, end_day+1):
        #  the sensor model is omitted to calculate probability of rain of 101 
        # and we use the probability upto the day 100
        # for eg: if we have probability upto day 2, the probability of rain on day 3 can be calculated as below
        # P(R2+k|U1, U2) = ⟨0.7, 0.3⟩P(r2+k−1|U1, U2) + ⟨0.3, 0.7⟩P(¬r2+k−1|U1, U2)
        # P(r2+k|U1, U2) = 0.7P(r2+k−1|U1, U2) + 0.3(1 − P(r2+k−1|U1, U2))
        #                = 0.4P(r2+k−1|U1, U2) + 0.3
        future_rain = 0.4*last_val+0.3 # we use the last equation to calculate the probabilities of day 101 to 150
        x_prob_rain.append(future_rain)
        last_val = future_rain

    return x_prob_rain

# following lines are main function:
evidence_data_add = "assign2_umbrella.txt"
start_day = 101
end_day = 150
# the prior distribution on the initial state, P(X0). 50% rainy, and 50% sunny on day 0.
prior = [0.5, 0.5]

x_prob_rain=prediction(evidence_data_add, prior, start_day, end_day)
for i in range(start_day, end_day+1):
    print("Day " + str(i) + ": rain " + str(x_prob_rain[i-start_day]) + ", sunny " + str(1 - x_prob_rain[i-start_day]))
#     print("Day " + str(i+1) + ": rain " + str(x_prob_rain[i]) + ", sunny " + str(1 - x_prob_rain[i]))


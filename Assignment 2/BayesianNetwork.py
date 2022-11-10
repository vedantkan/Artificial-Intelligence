#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

def get_p_b_cd():
    # Create 3 matrix of size 3x2
    p_b_cd = np.zeros((3,3,2),dtype = float)
    # Using a for loop to iterate over 3 values of b
    for b in range(1,p_b_cd.shape[0]+1):
        # Using a for loop to iterate over 3 values of c
        for c in range(1,p_b_cd.shape[1]+1):
            # Using a for loop to iterate over 2 values of d
            for d in range(1,p_b_cd.shape[2]+1):
                # Count and store the total number of times 'c' and 'd' have the values of c(from the loop) 
                # and d(from the loop)
                count_total = np.sum((data["c"]==c) & (data["d"]==d))
                # Now count and store the total number of times 'b' has the value b (from the loop)  
                # when 'c' and 'd' have values c(from the loop) and d(from the loop)
                count_b = np.sum((data["b"]==b) & (data["c"]==c) & (data["d"]==d))
                # On dividing the count of b occurences by the total occurences of c & d 
                # we get the probability of 'b' = b when 'd' = d and 'c' = c
                p_b_cd[b-1,c-1,d-1] = count_b / count_total
    return p_b_cd


def get_p_a_be():
    # Create 2 matrix of size 3x2
    p_a_be = np.zeros((2,3,2),dtype = float)
    # Using a for loop to iterate over 2 values of a
    for a in range(1,p_a_be.shape[0]+1):
        # Using a for loop to iterate over 3 values of b
        for b in range(1,p_a_be.shape[1]+1):
            # Using a for loop to iterate over 2 values of e
            for e in range(1,p_a_be.shape[2]+1):
                # Count and store the total number of times 'b' and 'e' have the values of b(from the loop)
                # and e(from the loop) 
                count_total = np.sum((data["b"] == b) & (data["e"] == e))
                # Now count and store the total number of times 'a' has the value a and e(from the loop) 
                # when 'b' and 'e' have values b (from the loop) and e (from the loop)
                # eg: a = 1 when b = 1 & e = 1, a = 2 when b = 1, e = 2
                count_a = np.sum((data["a"] == a) & (data["b"] == b) & (data["e"] == e))
                # On dividing the count of a occurences by the total occurences of b & e 
                # we get the probability of 'a' = a (from the loop) when 'b' = b (from the loop) 
                # and 'e' = e (from the loop)
                p_a_be[a - 1, b - 1, e - 1] = float(count_a) / float(count_total)
    return p_a_be


# following lines are main function:
data_add = open("assign2_BNdata.txt")
data = pd.read_csv(data_add, delimiter=r'\s+')
m = data.shape[0]
if __name__ == '__main__':


    # probability distribution of b.
    p_b_cd = get_p_b_cd()
    for c in range(3):
        for d in range(2):
            for b in range(3):
                print("P(b=" + str(b + 1) + "|c=" + str(c + 1) + ",d=" + str(d + 1) + ")=" + str(p_b_cd[b][c][d]))

    # probability distribution of a.
    p_a_be = get_p_a_be()
    for b in range(3):
        for e in range(2):
            for a in range(2):
                print("P(a=" + str(a + 1) + "|b=" + str(b  + 1) + ",e=" + str(e + 1) + ")=" + str(p_a_be[a][b][e]))


# In[ ]:





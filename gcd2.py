# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 13:32:49 2019

Author:Mwangi
Purpose: A program to get gcd and hcf Using Euclidean Algorithm that takes 3 arguments
"""
# using Euclidean Algorithm

def Findgcd(x,y,z):
    while(y):
        #x, z = z, x % z and x, y = y, x % x
        
         x, y = y, x % y
         x, z = z, x % z  # ***debatable not accurate please make it accurate?
    return x  

i = 210
j = 420
h = 630

print ("the gcd of 210 420 630 is:" , end = "")
print (Findgcd(210, 420, 630))  

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:47:20 2019

Author:Mwangi
Purpose: A program to get gcd , this program takes 3 arguments 
the main purpose is to write a program that can take ... n arguments
"""
def findgcd(x,y,z):
    if x > y:
        number = y, z
    else:
        number = x

        
    for i in range (1, number+1):
        if((x % i == 0) and (y % i == 0) and (z % i == 0)):
            gcd = i
            
    return gcd

i = 330
j = 462
h = 792

print ("the gcd for 330,462,792 is: ", end="" )
print (findgcd(330,462,792))        
    
        
        
                
        


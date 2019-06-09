# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 20:47:20 2019
Author:Sharad_Bhardwaj and mwangi  
a simple program for rounding the nearest tens
"""
# Python3 code to round the given  
# integer to a whole number  
# which ends with zero. 

# function to round the number 
def round( n ): 

    # Smaller multiple 
    a = (n // 100) * 100

    # Larger multiple 
    b = a + 100

    # Return of closest of two 
    return (b if n - a > b - n else a) 

# driver code 
n = int(input("Enter Real Numbers >= 1 ... n : "))
print(round(n)) 

# This code is contributed by "Sharad_Bhardwaj".
# The input valu codetributed mwangi 
    
    


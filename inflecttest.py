# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 19:27:19 2019

@author: mwangi

"""
# pip install inflect 

import inflect
p = inflect.engine()
p.number_to_words(12345698)

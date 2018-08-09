# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 13:08:39 2018

@author: s-siraki
"""

class calculator:
    
    def lexer(formula_str):
        formula_chars = list(formula_str)
        num = 0
        formula_list = list()
        for item in formula_chars:
            if 0<= int(item) <=9:
                num = num*10 + int(item)
            else:
                formula_list.append(num)
                formula_list.append(item)
                num = 0
        return formula_list
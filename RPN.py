# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 10:20:15 2018

@author: s-siraki
"""

class RPNConverter:
    
    def __init__(self,formula_str):
        self.formula_str = formula_str
        self.RPNformula = self.RPNconvert(self.lexer(formula_str))
        
        
    def lexer(self,formula_str):
        formula_chars = list(formula_str)
        num = 0
        formula_list = list()
        for item in formula_chars:
            if item.isdigit() :
                num = num*10 + int(item)
            else:
                formula_list.append(num)
                formula_list.append(item)
                num = 0
        return formula_list
    
    def RPNconvert(self,formula_list):
        RPNformula = list()
        op_stack = list()
        for item in formula_list:
            if isinstance(item,int):
                RPNformula.append(item)
            elif item =='+' | item == '-':
                 RPNformula.append(item)
            elif item == '=':
                for i in range(len(op_stack)-1):
                    RPNformula.append(op_stack.pop())
                RPNformula.append(item) 
        print(RPNformula)
        return RPNformula
    
    def getRPNformula(self):
        return self.RPNformula
    
    def getFormula_str(self):
        return self.formula_str
    
    
class RPNCalcurator:
    
    def __init__(self,RPNformula):
        self.ans = self.RPNcalculate(RPNformula)
        
    
    def RPNcalculate(self,RPNformula):
        num_stack = list()
        ans = 0
        for item in RPNformula:
            if item.isdigit():
                num_stack.append(item)
            elif not item == '=':
                num_stack.append(self.calc(num_stack.pop(-2),num_stack.pop(-1),item))
            else:
                ans = num_stack.pop()
        return ans
                
            
    def calc(a,b,op):
        if op == '+':
            return a+b
        elif op == '-':
            return a-b
        return 0
        
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 00:03:55 2023

@author: Thiago Carlos
"""

def list2string(variable):
    string = ''
    for i in variable:
        string += i
    return string


def string2list(variable):
    outList = []
    for i in variable:
        outList.append(i)
    return outList
        
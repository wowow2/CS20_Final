#CheckNumerics.py
'''
title: Computing Science Project B (Check Numeric functions File)
author: Abbas Rizvi
date: 2022/05/27
'''

### --- FUNCTIONS --- ###
def checkNumeric1(string):
    """
    Checks if an input is numeric as well checking if a number is negetive or not

    :param: string (Postional Argument)
    """
    ALERT = True
    try:
        NUMBER = float(string)
    except ValueError:
        ALERT = False
        NUMBER = -999

    if NUMBER < 0:
        ALERT = False
    else:
        ALERT = True

    return ALERT

def checkNumeric2(string):
    """
    Checks if an input is numeric

    :param: string (Postional Argument)
    """
    ALERT = True
    try:
        NUMBER = float(string)
    except ValueError:
        ALERT = False

    return ALERT

def checkNumeric3(string):
    """
    Checks if an input is numeric as well as checking if it is 0 or less 

    :param: string (Postional Argument)
    """
    
    ALERT = True
    try:
        NUMBER = float(string)
    except ValueError:
        ALERT = False
        NUMBER = -999

    if NUMBER <= 0:
        ALERT = False
    else:
        ALERT = True

    return ALERT
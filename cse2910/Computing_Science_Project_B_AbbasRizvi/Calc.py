#Calculations.py
'''
title: Computing Science Project B (Calculations File)
author: Abbas Rizvi
date: 2022/05/27
'''

### --- IMPORTS --- ###
import math

### --- FUNCTIONS --- ###
def CalcGrowthRate(FinalPop, InitialPop, ElapsedTime):
    """
    Takes the Final Population, Initial Population and Time Elapsed from the user and calculates
    the Growth Rate

    :param: FinalPop (Postional Argument)
    :param: InitialPop (Postional Argument)
    :param: ElapsedTime (Positional Arugment)

    :return: Growth_Rate_Percent (int)
    """

    Growth_Rate = ((FinalPop/InitialPop)**(1/ElapsedTime))-1

    Growth_Rate_Percent = Growth_Rate * 100

    return Growth_Rate_Percent

def CalcInitialPop(FinalPop, GrowthRate, ElapsedTime):
    """
    Takes the Final Population, Growth Rate and Time Elapsed from the user and calculates
    the Initial Population

    :param: FinalPop (Postional Argument)
    :param: GrowthRate (Postional Argument)
    :param: ElapsedTime (Positional Arugment)

    :return: Initial_Pop (int)
    """

    GrowthRate = GrowthRate/100
    Inital_Pop = FinalPop/((1+GrowthRate)**(ElapsedTime))
    Inital_Pop = round(Inital_Pop, 0)
    
    return Inital_Pop 

def CalcFinalPop(InitialPop,GrowthRate, ElapsedTime):
    """
    Takes the Growth Rate, Initial Population and Time Elapsed from the user and calculates
    the Final Population

    :param: InitialPop (Postional Argument)
    :param: GrowthRate (Postional Argument)
    :param: ElapsedTime (Positional Arugment)

    :return: Final_Pop (int)
    """

    GrowthRate = GrowthRate/100
    Final_Pop = InitialPop * ((1+GrowthRate)**(ElapsedTime))
    Final_Pop = round(Final_Pop, 0)
    return Final_Pop 

def CalcElapsedTime(InitialPop, GrowthRate, FinalPop):
    """
    Takes the Growth Rate, Initial Population and Final Population from the user and calculates
    the Time Elapsed

    :param: InitialPop (Postional Argument)
    :param: GrowthRate (Postional Argument)
    :param: FinalPop (Positional Arugment)

    :return: Elapsed_Time (int)
    """

    GrowthRate = GrowthRate/100
    Elapsed_Time = (math.log(FinalPop/InitialPop))/(math.log(1+GrowthRate))
    Elapsed_Time = round(Elapsed_Time, 0)
    return Elapsed_Time 

def CalcDT(GrowthRate):
    """
    Calculates the doubling time using the growth rate given by the user or calculated 
    using other inputs from the user

    :param: GrowthRate (Postional Argument)

    :return: Doubling_Time (int)
    """
    if GrowthRate == 0:
        Doubling_Time = "Undefined"
    else:
        GrowthRate = GrowthRate/100
        Doubling_Time = (math.log(2)/math.log(1+GrowthRate))
        Doubling_Time = round(Doubling_Time, 2)
    
    return Doubling_Time

def CalcHL(ElapsedTime, FinalPop, InitialPop):
    """
    Calculates the half time using the Time Elapsed, Final Population and Initial Population given by the user or calculated 
    using other inputs from the user

    :param: ElapsedTime (Postional Argument)
    :param: FinalPop (Postional Argument)
    :param: InitialPop (Postional Argument)

    :return: Half_Life (int)
    """
    if FinalPop == InitialPop:
        Half_Life = "Undefined"
    else:
        Half_Life = ElapsedTime/(math.log(FinalPop/InitialPop)/math.log(1/2))
        Half_Life = round(Half_Life, 2)
    
    return Half_Life

def CheckGrowthRate(GrowthRate, InitialPop, FinalPop):
    """
    Checks if the set of data needs a half-life or a doubling time value
    
    :param: GrowthRate (Postional Argument)
    :param: InitialPop (Postional Argument)
    :param: FinalPop (Postional Argument)

    :returns: Postive_GrowthRate (bool)
    """
    Positive_GrowthRate = True

    if GrowthRate < 0:
        Positive_GrowthRate = False
    
    if InitialPop > FinalPop:
        Positive_GrowthRate = False

    return Positive_GrowthRate


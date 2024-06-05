#Database-.py
'''
title: Computing Science Project B (Database File)
author: Abbas Rizvi
date: 2022/05/27
'''

### --- IMPORTS --- ###
import sqlite3
from Main import DB_NAME
import Calc as Pr

### --- VARIABLES --- ###
BACTERIA_DATA = []

### --- FUNCTIONS --- ###
def CreateTable():
    """
    Creates the sqlite database which stores the user's calculations
    """

    global DB_NAME
    CONNECTION = sqlite3.connect(DB_NAME)
    CURSOR = CONNECTION.cursor()

    CURSOR.execute('''
        CREATE TABLE
            Bacteria_Data(
                Bacteria_Name TEXT NOT NULL,
                Initial_Population TEXT,
                Final_Population TEXT,
                Growth_Rate TEXT,
                Elapsed_Time TEXT,
                Doubling_Time TEXT,
                Half_Life TEXT
            )
        
    ;''')
    CONNECTION.commit()
    CONNECTION.close()

@staticmethod
def SaveData(Bacteria_Name):
    """
    This function takes the data from the calculation and puts it into the database

    :param: Bacteria_Name (Postional Argument)
    """
    global DB_NAME
    CONNECTION = sqlite3.connect(DB_NAME)
    CURSOR = CONNECTION.cursor()

    BACTERIA_DATA.insert(0, Bacteria_Name)
    CURSOR.execute('''
        INSERT INTO
            Bacteria_Data
        VALUES(
            ?,?,?,?,?,?,?
            )
        ;''', BACTERIA_DATA)
        
    print("Data Saved Sucessfully")
    CONNECTION.commit()
    CONNECTION.close()

def StoreData(INITIAL_POP,FINAL_POP,GROWTH_RATE, ELAPSED_TIME):
    """
    This function stores the calculation data into a list based on if half-life or doubling time
    applies, this data is eventually put into the database.

    :param: INITIAL_POP (Postional Argument)
    :param: FINAL_POP (Postional Argument)
    :param: GROWTH_RATE (Postional Argument)
    :param: ELAPSED_TIME (Postional Argument)
    """
    if Pr.CheckGrowthRate(GROWTH_RATE, INITIAL_POP, FINAL_POP):
        DOUBLING_TIME = Pr.CalcDT(GROWTH_RATE)
        GROWTH_RATE = round(GROWTH_RATE, 2)
        
        if (GROWTH_RATE == 0.0 and DOUBLING_TIME == "Undefined"):
            DOUBLING_TIME = "NA"
        BACTERIA_DATA.append(INITIAL_POP)
        BACTERIA_DATA.append(FINAL_POP)
        BACTERIA_DATA.append(f"{GROWTH_RATE}%")
        BACTERIA_DATA.append(ELAPSED_TIME)
        BACTERIA_DATA.append(DOUBLING_TIME)
        BACTERIA_DATA.append("NA")

    else:
        HALF_LIFE = Pr.CalcHL(ELAPSED_TIME, FINAL_POP, INITIAL_POP)
        GROWTH_RATE = round(GROWTH_RATE, 2)

        BACTERIA_DATA.append(INITIAL_POP)
        BACTERIA_DATA.append(FINAL_POP)
        BACTERIA_DATA.append(f"{GROWTH_RATE}%")
        BACTERIA_DATA.append(ELAPSED_TIME)
        BACTERIA_DATA.append("NA")
        BACTERIA_DATA.append(HALF_LIFE)

def getallbacterias():
    """
    Selects everything in the database so that it can be transported to the HTML pages

    :returns: BACTERIAS (Sqlite Cursor)
    """
    global DB_NAME
    CONNECTION = sqlite3.connect(DB_NAME)
    CURSOR = CONNECTION.cursor()

    BACTERIAS = CURSOR.execute('''
        SELECT
            *
        FROM 
            Bacteria_Data
        ORDER BY
            Bacteria_Name
    ;''').fetchall()
    CONNECTION.close()

    return BACTERIAS
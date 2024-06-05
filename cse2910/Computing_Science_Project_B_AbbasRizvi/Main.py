#Main.py

'''
title: Computing Science Project B (Main File)
author: Abbas Rizvi
date: 2022/05/13
'''

### --- IMPORTS --- ###
import CheckNumerics as cn #File for functions which check if the user input is valid
import Calc as cl #File for functions which use the user inputs and perform calculations
import Database as db #File f
from pathlib import Path
import flask as fl

### --- VARIABLES --- ###
DB_NAME = "Calc.db"
FIRST_RUN = True
if (Path.cwd()/DB_NAME).exists():
    FIRST_RUN = False

### --- HTML COMPONENT --- ###
app = fl.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    This is this homepage for the calculator, the page will offer information about what the
    calculator does, how it works and the different calculations that can be done based around
    exponential growt/decay of bacteria.

    :returns: (HTML Page)
    """
    return fl.render_template("index.html")

@app.route('/GRCalc', methods=['GET', 'POST'])
def GrowthRateCalc():
    """
    This is the page where the user can calculate the growth rate of a bacteria and view their
    previous calculations

    :returns: (HTML Page)
    """

    ALERT = ""
    if fl.request.form:
        db.BACTERIA_DATA = []
        BACTERIA_NAME = fl.request.form.get("bacteria_name")
        INITIAL_POPULATION = fl.request.form.get("initial_population")
        FINAL_POPULATION = fl.request.form.get("final_population")
        TIME_ELAPSED = fl.request.form.get("time")

        CHECKNUMERIC1 = cn.checkNumeric1(INITIAL_POPULATION)
        CHECKNUMERIC2 = cn.checkNumeric1(FINAL_POPULATION)
        CHECKNUMERIC3 = cn.checkNumeric3(TIME_ELAPSED)
        ALERT0 = ""
        ALERT1 = ""
        ALERT2 = ""
        ALERT3 = ""

        if BACTERIA_NAME == "":
            ALERT0 = f"Bacteria ID must be provided."

        if not CHECKNUMERIC1:
            ALERT1 = f"Initial Population must be a postive number."

        if not CHECKNUMERIC2:
            ALERT2 = f"Final Population must be a postive number."

        if not CHECKNUMERIC3:
            ALERT3 = f"Elapsed Time must be greater than 0."

        if (CHECKNUMERIC1 and CHECKNUMERIC2 and CHECKNUMERIC3 and BACTERIA_NAME != ""):
            GROWTH_rate = cl.CalcGrowthRate(float(FINAL_POPULATION),float(INITIAL_POPULATION),float(TIME_ELAPSED))
            db.StoreData(float(INITIAL_POPULATION), float(FINAL_POPULATION),float(GROWTH_rate),float(TIME_ELAPSED))
            db.SaveData(BACTERIA_NAME)
            
            if db.BACTERIA_DATA[6] == "NA":
                ALERT = f"The Growth Rate is {db.BACTERIA_DATA[3]} and the Doubling Time is {db.BACTERIA_DATA[5]} Seconds. Successfully added!"
            else:
                ALERT = f"The Growth Rate is {db.BACTERIA_DATA[3]} and the Half-Life is {db.BACTERIA_DATA[6]} Seconds. Successfully added!"
  
        else:
            ALERT = ALERT0 +" "+ALERT1 +" "+ ALERT2 +" "+ ALERT3
    
    QUERY_BACTERIAS = db.getallbacterias()
    return fl.render_template("GRinterface.html", alert = ALERT, BACTERIAS = QUERY_BACTERIAS)

@app.route('/IPCalc', methods=['GET', 'POST'])
def InitialPopCalc():
    """
    This is the page where the user can calculate the initial population of a bacteria and view their
    previous calculations

    :returns: (HTML Page)
    """

    ALERT = ""
    if fl.request.form:
        db.BACTERIA_DATA = []
        BACTERIA_NAME = fl.request.form.get("bacteria_name")
        GROWTH_rate = fl.request.form.get("growth_rate")
        FINAL_POPULATION = fl.request.form.get("final_population")
        TIME_ELAPSED = fl.request.form.get("time")

        CHECKNUMERIC1 = cn.checkNumeric2(GROWTH_rate)
        CHECKNUMERIC2 = cn.checkNumeric1(FINAL_POPULATION)
        CHECKNUMERIC3 = cn.checkNumeric3(TIME_ELAPSED)
        ALERT0 = ""
        ALERT1 = ""
        ALERT2 = ""
        ALERT3 = ""

        if BACTERIA_NAME == "":
            ALERT0 = f"Bacteria ID must be provided."

        if not CHECKNUMERIC1:
            ALERT1 = f"Growth Rate must be a number."

        if not CHECKNUMERIC2:
            ALERT2 = f"Final Population must be a postive number."

        if not CHECKNUMERIC3:
            ALERT3 = f"Elapsed Time must be greater than 0."

        if (CHECKNUMERIC1 and CHECKNUMERIC2 and CHECKNUMERIC3 and BACTERIA_NAME != ""):
            INITIAL_POPULATION = cl.CalcInitialPop(float(FINAL_POPULATION),float(GROWTH_rate),float(TIME_ELAPSED))
            db.StoreData(float(INITIAL_POPULATION), float(FINAL_POPULATION),float(GROWTH_rate),float(TIME_ELAPSED))
            db.SaveData(BACTERIA_NAME)

            if db.BACTERIA_DATA[6] == "NA":
                if (float(GROWTH_rate) == 0 and db.BACTERIA_DATA[5] == "NA"):
                    ALERT = f"The Initial Population is {db.BACTERIA_DATA[1]} Cells and the Doubling Time or Half Life cannot be calculated"
                else:
                    ALERT = f"The Initial Population is {db.BACTERIA_DATA[1]} Cells and the Doubling Time is {db.BACTERIA_DATA[5]} Seconds"
            else:
                ALERT = f"The Initial Population is {db.BACTERIA_DATA[1]} Cells and the Half-Life is {db.BACTERIA_DATA[6]} Seconds"
        else:
            ALERT = ALERT0 +" "+ ALERT1 +" "+ ALERT2 +" "+ ALERT3
    
    QUERY_BACTERIAS = db.getallbacterias()
    return fl.render_template("IPinterface.html", alert = ALERT, BACTERIAS = QUERY_BACTERIAS)

@app.route('/FPCalc', methods=['GET', 'POST'])
def FinalPopCalc():
    """
    This is the page where the user can calculate the final population of a bacteria and view their
    previous calculations

    :returns: (HTML Page)
    """

    ALERT = ""
    if fl.request.form:
        db.BACTERIA_DATA = []
        BACTERIA_NAME = fl.request.form.get("bacteria_name")
        GROWTH_rate = fl.request.form.get("growth_rate")
        INITIAL_POPULATION = fl.request.form.get("initial_population")
        TIME_ELAPSED = fl.request.form.get("time")

        CHECKNUMERIC1 = cn.checkNumeric2(GROWTH_rate)
        CHECKNUMERIC2 = cn.checkNumeric1(INITIAL_POPULATION)
        CHECKNUMERIC3 = cn.checkNumeric3(TIME_ELAPSED)
        ALERT0 = ""
        ALERT1 = ""
        ALERT2 = ""
        ALERT3 = ""

        if BACTERIA_NAME == "":
            ALERT0 = f"Bacteria ID must be provided."

        if not CHECKNUMERIC1:
            ALERT1 = f"Growth rate must be a number."

        if not CHECKNUMERIC2:
            ALERT2 = f"Initial Population must be a postive number."

        if not CHECKNUMERIC3:
            ALERT3 = f"Elapsed Time must be greater than 0."

        if (CHECKNUMERIC1 and CHECKNUMERIC2 and CHECKNUMERIC3 and BACTERIA_NAME != ""):
            FINAL_POPULATION = cl.CalcFinalPop(float(INITIAL_POPULATION),float(GROWTH_rate),float(TIME_ELAPSED))
            db.StoreData(float(INITIAL_POPULATION), float(FINAL_POPULATION),float(GROWTH_rate),float(TIME_ELAPSED))
            db.SaveData(BACTERIA_NAME)

            if db.BACTERIA_DATA[6] == "NA":
                if (float(GROWTH_rate) == 0 and db.BACTERIA_DATA[5] == "NA"):
                    ALERT = f"The Final Population is {db.BACTERIA_DATA[2]} Cells and the Doubling Time or Half Life cannot be calculated"
                else:
                    ALERT = f"The Final Population is {db.BACTERIA_DATA[2]} Cells and the Doubling Time is {db.BACTERIA_DATA[5]} Seconds"
            else:
                ALERT = f"The Final Population is {db.BACTERIA_DATA[2]} Cells and the Half-Life is {db.BACTERIA_DATA[6]} Seconds"
        else:
            ALERT = ALERT0+" "+ALERT1 +" "+ ALERT2 +" "+ ALERT3
    
    QUERY_BACTERIAS = db.getallbacterias()
    return fl.render_template("FPinterface.html", alert = ALERT, BACTERIAS = QUERY_BACTERIAS)

@app.route('/ETCalc', methods=['GET', 'POST'])
def ElapsedTimeCalc():
    """
    This is the page where the user can calculate the time elapsed of a bacteria and view their
    previous calculations

    :returns: (HTML Page)
    """

    ALERT = ""
    if fl.request.form:
        db.BACTERIA_DATA = []
        BACTERIA_NAME = fl.request.form.get("bacteria_name")
        GROWTH_rate = fl.request.form.get("growth_rate")
        INITIAL_POPULATION = fl.request.form.get("initial_population")
        FINAL_POPULATION = fl.request.form.get("final_population")

        CHECKNUMERIC1 = cn.checkNumeric2(GROWTH_rate)
        CHECKNUMERIC2 = cn.checkNumeric1(INITIAL_POPULATION)
        CHECKNUMERIC3 = cn.checkNumeric1(FINAL_POPULATION)
        ALERT0 = ""
        ALERT1 = ""
        ALERT2 = ""
        ALERT3 = ""

        if BACTERIA_NAME == "":
            ALERT0 = f"Bacteria ID must be provided."

        if not CHECKNUMERIC1:
            ALERT1 = f"Growth rate must be a number."

        if not CHECKNUMERIC2:
            ALERT2 = f"Initial Population must be a postive number."

        if not CHECKNUMERIC3:
            ALERT3 = f"Final Population must be a postive number."

        if (CHECKNUMERIC1 and CHECKNUMERIC2 and CHECKNUMERIC3 and BACTERIA_NAME != ""):

            if (float(GROWTH_rate) > 0 and float(FINAL_POPULATION) <= float(INITIAL_POPULATION)):
                ALERT = f"Data is incorrect, with a postive growth rate, the final population must be greater than the initial population."
            elif (float(GROWTH_rate) < 0 and float(FINAL_POPULATION) >= float(INITIAL_POPULATION)):
                ALERT = f"Data is incorrect, with a negative growth rate, the final population must be less than the initial population."
            elif (float(GROWTH_rate) == 0):
                ALERT = ALERT = f"Data is incorrect, the growth rate must be a non-zero number. Therefore, time elapsed cannot be calculated"
            else:
                TIME_ELAPSED = cl.CalcElapsedTime(float(INITIAL_POPULATION),float(GROWTH_rate),float(FINAL_POPULATION))
                db.StoreData(float(INITIAL_POPULATION), float(FINAL_POPULATION),float(GROWTH_rate),float(TIME_ELAPSED))
                db.SaveData(BACTERIA_NAME)

                if db.BACTERIA_DATA[6] == "NA":
                    ALERT = f"The Time Elapsed is {db.BACTERIA_DATA[4]} Seconds and the Doubling Time is {db.BACTERIA_DATA[5]} Seconds"
                else:
                    ALERT = f"The Time Elapsed is {db.BACTERIA_DATA[4]} Seconds and the Half-Life is {db.BACTERIA_DATA[6]} Seconds"

        else:
            ALERT = ALERT0 + " " +ALERT1 +" "+ ALERT2 +" "+ ALERT3
    
    QUERY_BACTERIAS = db.getallbacterias()
    return fl.render_template("ETinterface.html", alert = ALERT, BACTERIAS = QUERY_BACTERIAS)


### --- MAIN --- ###
if __name__ == "__main__":
    if FIRST_RUN:
        db.CreateTable()
    app.run(debug = False)
        


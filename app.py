# import imp
# import re
from flask import Flask, request, url_for, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from datetime import datetime
# from sympy import Symbol,symbols, Function,diff, Eq, dsolve, solve, lambdify
import numpy as np
import matplotlib.pyplot as plt
from werkzeug.debug import DebuggedApplication
# from matplotlib.animation import FuncAnimation
# from time import time
# import math
# from functools import partial
import os
import mpld3
from pyXSteam.XSteam import XSteam

# os.sys.path.append("C:\\Users\\apsta\\PycharmProjects\\pythonProject")
# import rownania_rozniczkowe


app = Flask(__name__, template_folder="Templates")

app.debug = True
app.config['SECRET_KEY'] = '1111'
# toolbar = DebugToolbarExtension(app)

@app.route('/')
def index():
    time_now = datetime.now().strftime('%H:%M:%S')
    return '<h1>Hello World!!!!: {}</h1><h1> debug = {}</h1>'.format(time_now, app.debug)
# Lekcja 2,9
@app.route('/currency/<amount>/<string:currency_from>/')
def currency(amount,currency_from):
    strona = """<h1> chcesz wymienić {} w ilości {}</h1?>""".format(currency_from.upper(), amount)
    return strona
# Lab 2,9
@app.route('/cook/<recepie>/<step>')
def cook(step,recepie):
    # na stronie mają być przyciski które kierują do następnej strony
    # jak się tylko dowiem jak te przyciski robić to wrócę do ćwiczenia
    pass

# Lekcja 2,10
# http://127.0.0.1:5000/cook/pomid/13?font-size=120%&color=blue
#  ? - początek query string
# & - kolejne parametry
# parametr=wartość
@app.route('/query_string/')
def query_string():
    fontSize = '22'
    newColor = 'black'
    for key in request.args:
        print(key, request.args[key],type(request.args[key]))
    # print(request.query_string)
    # return '<h1>Hello query stringi = {}!!!!</h1>'.format(request.query_string)
    if 'font-size' in request.args:
        fontSize = request.args['font-size']
        print("font-size")
    if 'color' in request.args:
        newColor = request.args['color']

    body = """<h1 style="font-size:{};color:{}"> Hello query stringi = {}!!!!</h1>\
        <p1 style="color:{};font-size:{}"> dupa </p1>""".format(fontSize,newColor,request.query_string, newColor,fontSize)  
    return body

# Lekcja 2,11
# obsługa formularzy
@app.route('/form_source')
def form_source():
    head = """
    <head>
        <style>
            output {
                border: 3px solid black;
                border-collapse: collapse;
                background-color: #96D4D4;
                }
        </style> 
    </head>"""
    body = """
    <form action="/form_target" method="POST" oninput="result.value=cars.value"> <!-- nie rozumiemiem tego co się dzieje w oninput, jakiś fragment kodu ale co gdzie i jak to nie mam pojęcia
                                                                                    skąd się biorą zmienne i jaki mają zasięg??? -->
        <input type="text" id="currency" name="currency" value="PLN">
        <label for="currency">Waluta</label><br>
        <input type="text" id="amount" name="amount" value="100">
        <label for="amount">Kwota</label><br>
        <select id="cars" name="cars" >
            <option value="skoda">Volvo</option>
            <option value="saab">Saab</option>
            <option value="fiat">Fiat</option>
            <option value="audi">Audi</option>
        </select><br>
        <output name="result">dummy</output><br>
        <input type="submit" value="Wyślij">
    </form><br>
    
    """
    return head+body

@app.route('/form_target', methods=['POST'])
def form_target():
    currency = "PLN"
    if "currency" in request.form:
        currency = request.form["currency"]
    amount = "1"
    if "amount" in request.form:
        amount = request.form["amount"]
    selected = '---'
    if "cars" in request.form:
        selected = request.form["cars"]
    return f"<h1>Wymieniasz {amount} waluty: {currency}; pole wyboru: {selected} </h1>"
    
# Lekcja 2,12
# GET i POST w jednym route
@app.route('/form__get_post', methods=['GET', 'POST'])
def form_get_post():
    if request.method == "GET":
        body = """
        <h1> Restart Test </h1>
        <form action="{}" method="POST">
            <input type="text" id="currency" name="currency" value="PLN">
            <label for="currency">Waluta</label><br>
            <input type="text" id="amount" name="amount" value="100">
            <label for="amount">Kwota</label><br>
            <select id="cars" name="cars" >
                <option value="skoda">Volvo</option>
                <option value="saab">Saab</option>
                <option value="fiat">Fiat</option>
                <option value="audi">Audi</option>
            </select><br>
            <input type="submit" value="Wyślij">
        </form><br>
        
        """.format(url_for("form_get_post",_external=True))
        return body
    else:
        currency = "PLN"
        if "currency" in request.form:
            currency = request.form["currency"]
        amount = "1"
        if "amount" in request.form:
            amount = request.form["amount"]
        selected = '---'
        if "cars" in request.form:
            selected = request.form["cars"]
        return f"<h1>Wymieniasz {amount} waluty: {currency}; pole wyboru: {selected} </h1>"


# Lekcja 2,13
# url_for
@app.route('/obrazek')
def obrazek():
    strona = f"""
        <body>
        <h1>Już wiem jak wskazać ścieżkę do pliku</h1>
        <img src={url_for('static', filename = "pot_with_earth.jpg", _external=True)} alt="nie wiem jak wskazać ścieżkę pliku :(">
        <!-- już wiem jak wskazać ścieżkę do pliku -->
        </body>"""
    return strona

@app.route('/url_for_nauka')
def url_for_nauka():
    strona = """
        <body>
        <a href="{}">obrazek</a><br>
        <a href="{}">index</a><br>
        </body>""".format(url_for("obrazek"),url_for("index"))
    return strona



# Lab 15
@app.route('/not_implemented/<message>)')
def not_implemented(message):
    return f"<h1>funkcja: {message} nieukończona, cierpliwośći kurwa!!!</h1>"

@app.route('/new_receipt')
def new_receipt():
    return redirect(url_for('not_implemented', message='/new_receipt' ))
    
@app.route('/old_receipt')
def old_receipt():
    return redirect(url_for('not_implemented', message='/old_receipt'))

# Lekjca 17
# set FLASK_ENV=development
# polecenie flask routes - jak się łatwo domyślić wyświetla routes z aplikacji

##########################################################
#element inercyjny I rzedu
@app.route('/inerc_I_row', methods=['GET','POST'])
def inerc_I_row():
    # def inercIorderSymb(T=1,K=1):
    #     T = T
    #     K = K
    #     t = Symbol('t')
    #     u = Symbol('u')
    #     y = Function('y')(t)
    #     dy = y.diff(t)
    #     diffEqParam = dy+y/T-K*u/T
    #     return diffEqParam, t, y, dy, u
    
    const_K, const_T, param_u, initial_t, initial_y, calc_time = 0,0,0,0,0,0
    body = f"""
    <form action="{url_for('inerc_I_row', _external=True)}" method="POST">
        <label for="const_K"> Stała K </label> <br>
        <input type="text" id="const_K" name="const_K" value="{const_K}"> <br>
        <label for="const_T"> tała T </label> <br>
        <input type="text" id="const_T" name="const_T" value="{const_T}"> <br>
        <label for="param_u"> Parametr u </label> <br>
        <input type="text" id="param_u" name="param_u" value="{param_u}"> <br>
        <label for="initial_t"> Warunki początkowe: t </label> <br>
        <input type="text" id="initial_t" name="initial_t" value="{initial_t}"> <br>
        <label for="calc_time"> Czas obliczeń </label> <br>
        <input type="text" id="calc_time" name="calc_time" value="{calc_time}"> <br>
        <label for="initial_y"> Warunki początkowe: y(t0) </label> <br>
        <input type="text" id="initial_y" name="initial_y" value="{initial_y}"> <br>
        <input type="submit" value="Zapisz"><br>
    """
    if request.method == "GET":
        return body
    else:
        if "const_T" in request.form:
            const_T = request.form["const_T"]
        if "const_K" in request.form:
            const_K = request.form["const_K"]
        if "param_u" in request.form:
            param_u = request.form["param_u"]
        if "initial_t" in request.form:
            initial_t = request.form["initial_t"]
        if "initial_y" in request.form:
            initial_y = request.form["initial_y"]
        if "calc_time" in request.form:
            calc_time = request.form["calc_time"]

        equationIorder, vInd, vDep, dvDep, param = rownania_rozniczkowe.inercIorderSymb(int(const_T), int(const_K))
        fUfunc1 = rownania_rozniczkowe.inercIorderSymbToUfunc(equationIorder, vInd, vDep, dvDep, param)
        t, y, rozn = rownania_rozniczkowe.myEuler(fUfunc1, int(param_u), int(initial_y), int(initial_t), int(calc_time))
        plt.figure()
        plt.plot(t,y)
        html_fig = mpld3.fig_to_html(plt.gcf())

        dane = f"""
        <p1> K = {const_K} </p1><br>
        <p1> T = {const_T} </p1><br>
        <p1> u = {param_u} </p1><br>
        <p1> t(0) = {initial_t} </p1><br>
        <p1> y(t(0)) = {initial_y} </p1><br>
        <p1> Czas obliczeń: {calc_time} </p1><br>
        <p1> {equationIorder} </p1><br>
        <p1> {fUfunc1(1,100,1)} </p1><br>
        <p1> {y} </p1><br>

        """
        body = f"""
        <form action="{url_for('inerc_I_row', _external=True)}" method="POST">
        <label for="const_K"> Stała K </label> <br>
        <input type="text" id="const_K" name="const_K" value="{const_K}"> <br>
        <label for="const_T"> tała T </label> <br>
        <input type="text" id="const_T" name="const_T" value="{const_T}"> <br>
        <label for="param_u"> Parametr u </label> <br>
        <input type="text" id="param_u" name="param_u" value="{param_u}"> <br>
        <label for="initial_t"> Warunki początkowe: t </label> <br>
        <input type="text" id="initial_t" name="initial_t" value="{initial_t}"> <br>
        <label for="calc_time"> Czas obliczeń </label> <br>
        <input type="text" id="calc_time" name="calc_time" value="{calc_time}"> <br>
        <label for="initial_y"> Warunki początkowe: y(t0) </label> <br>
        <input type="text" id="initial_y" name="initial_y" value="{initial_y}"> <br>
        <input type="submit" value="Zapisz"><br>
        """
        return body+dane+html_fig
    
##########################################################
# tablice parowe
# arguments = {"t":"temperature", "p":"pressure", "rho": "density", "h": "enthalpy", "s":"entrophy"}
globalnyLicznik=0
funkcja, varForPlot = "", ""
tempObliczen, cisnObliczen, zakresMin, zakresMax = 100.0, 5.0, 0.0, 100.0

class variable():
    def __init__(self, name, prompt, minValue = np.NINF, maxValue = np.inf, startValue = 0, abbrev = None, unit = None):
        self.name = name
        self.prompt = prompt.title()
        self.minVal = minValue
        self.maxVal = maxValue
        self.value = startValue
        if abbrev == None: 
            self.abbrev = name 
        else: 
            self.abbrev = abbrev
        self.unit = unit
        self.varForPlot = False
    def __str__(self):
        return f"Variable: {self.name}, start value = {self.value}, abbreviation name: {self.abbrev}, prompt: {self.prompt}"

# temp = variable('t', "Enter temperature value", 100, 'temp')
inputVar = {"t": variable('t', "Enter temperature value: ",0.0, 400.0, 100.0, 'temp', "\N{DEGREE SIGN}C" )}
inputVar.update({"p": variable('p', "Enter absolute pressure value: ",0.0 ,50.0, 5.0, 'press', "bar" )})
inputVar.update({"h": variable('h', "Enter enthalpy value: ", abbrev='enthalpy', unit="kJ/kg" )})
inputVar.update({"s": variable('s', "Enter entropy value", abbrev='entropy', unit="kJ/(kg \N{DEGREE SIGN}C)" )})
inputVar.update({"rho": variable('rho', "Enter density value", startValue=1000, unit="kg/m^3" )})
inputVar.update({"x": variable('x', "Enter vapour fraction value: ", 0.0, 100.0, 0.0, 'vapour', unit="%")})

outputVar = {"t": variable('t', "Enter temperature value: ",0.0, 400.0, 100.0, 'temp', "\N{DEGREE SIGN}C" )}
outputVar.update({"p": variable('p', "Enter absolute pressure value: ",0.0 ,50.0, 5.0, 'press', "bar" )})
outputVar.update({"h": variable('h', "Enter enthalpy value: ", abbrev='enthalpy', unit="kJ/kg" )})
outputVar.update({"s": variable('s', "Enter entropy value", abbrev='entropy', unit="kJ/(kg \N{DEGREE SIGN}C)" )})
outputVar.update({"Cp": variable('Cp', "Enter heat capacity value", abbrev='heat capacity', unit="kJ/(kg \N{DEGREE SIGN}C)" )})
outputVar.update({"Cv": variable('Cv', "Enter isochoric heat capacity value", abbrev='isochoric heat capacity', unit="kJ/(kg \N{DEGREE SIGN}C)" )})
outputVar.update({"rho": variable('rho', "Enter density value", startValue=1000, unit="kg/m^3" )})
outputVar.update({"v": variable('v', "Enter specific volume value: ", abbrev='specific volume', unit="m^3/kg")})
outputVar.update({"u": variable('u', "Enter internal energy value: ", abbrev='internal energy', unit="kJ/kg" )})
outputVar.update({"w": variable('w', "Enter speed of sound value: ", abbrev='speed of sound', unit="m/s" )})
outputVar.update({"tc": variable('tc', "Enter thermal conductivity", abbrev='thermal conductivity', unit="W/(m \N{DEGREE SIGN}C)" )})
outputVar.update({"st": variable('st', "Enter surface tension value: ", abbrev='surface tension', unit="N/m" )})
outputVar.update({"my": variable('my', "Enter viscosit value: ", abbrev='viscosity', unit="N*s/m^2" )})



@app.route('/tablice_parowe', methods=['GET', 'POST'])
def tablice_parowe():
    import matplotlib.pyplot as pyplot
    import numpy as np
    from pyXSteam.XSteam import XSteam

    global globalnyLicznik, funkcja, varForPlot, tempObliczen, cisnObliczen, zakresMin, zakresMax
    ## wybór funkcji - popup menue (POST)
    print(f"pracuje :) {globalnyLicznik}")
    globalnyLicznik += 1
    licznik = f"<br><br><br><p1> naliczyłem: {globalnyLicznik}</p1>"
    input_p, input_t = 'disabled', 'disabled'
    steam_function = f"""
    <form action="{url_for('tablice_parowe', _external=True)}", method="POST">
        <label for="function"> Wybierz funkcję: </label>
        <select id="function" name="function" >
            <option value="tsat_p">Temp. nasycenia (p abs)</option>
            <option value="hV_p">Entalpia pary nasyconej (p abs)</option>
            <option value="hV_t">Entalpia pary nasyconej (t) </option>
            <option value="h_pt">Entalpia (p abs, t)</option>
            <option value="rho_pt"> Gęstość (p abs, t)</option>    
        </select><br>
        <input type="submit" value="Zapisz"><br><br>
    </form>
    """
    value = f"""
    <form action="{url_for('tablice_parowe')}", method="POST">
        <label for="zadana_temp"> Podaj temperaturę do obiczeń </label>
        <input type="text", id="zadana_temp", name="zadana_temp", value="{tempObliczen}"><br>
        <label for="zadane_cisn"> Podaj ciśnienie (abs) do obiczeń </label>
        <input type="text", id="zadane_cisn", name="zadane_cisn", value="{cisnObliczen}"><br>
        <label for="zakres_min"> Zakres wykresu - min: </label>
        <input type="text", id="zakres_min", name="zakres_min", value="{zakresMin}"><br>
        <label for="zakres_max"> Zakres wykresu - max: </label>
        <input type="text", id="zakres_max", name="zakres_max", value="{zakresMax}"><br>
        <input type="submit" value="Oblicz"><br>
    </form>
    """
    selectForPlot = f"""
    <form action="{url_for('tablice_parowe')}", method="POST">
        <input type="radio", id="plotTemp", name="varForPlot", value="selectedTemp">
        <lable for="plotTemp"> Generuj wykres dla temperatury </label><br>
        <input type="radio", id="plotPres", name="varForPlot", value="selectedPres">
        <lable for="plotPres"> Generuj wykres dla ciśnienia </label><br>
        <input type="submit", value="Wybieram"><br><br>
    </form>
    """
    if request.method == "GET":
        return steam_function+value+selectForPlot+licznik
    # w zlażności o wybranje funkcji wybór zmiennych wejściowych: temp, ciśnienie, oba (GET)
    else:
        hasiok=""
        wyborFunkcjiOk, zadanaTempOk, zadaneCisnOk, zakresMinOk, zakresMaxOk, varForPlotOk = "", "", "", "", "", ""
        
        tempObliczen, 
        if "function" in request.form and request.form["function"] != None:
            funkcja = request.form.get("function")
            wyborFunkcjiOk = f"<p1> Funkjca wybarana poprawnie: {funkcja}</p1><br>"
        if "zadana_temp" in request.form:
            tempObliczen = float(request.form.get("zadana_temp"))
            zadanaTempOk = f"<p1> Temp. do obliczeń: {str(tempObliczen)}<br>"
        if "zadane_cisn" in request.form:
            cisnObliczen = float(request.form.get("zadane_cisn"))
            zadaneCisnOk = f"<p1> Ciśnienie do obliczeń: {str(cisnObliczen)}<br>"
        if "zakres_min" in request.form:
            zakresMin = float(request.form.get("zakres_min"))
            zakresMinOk = f"<p1> Zakres min dla wykresu: {str(zakresMin)}<br>"
        if "zakres_max" in request.form:
            zakresMax = float(request.form.get("zakres_max"))
            zakresMaxOk = f"<p1> Zakres max dla wykresu: {str(zakresMax)}<br>"
        if "varForPlot" in request.form:
            varForPlot = request.form.get("varForPlot")
            varForPlotOk = f"<p1> Zmienna dla wykresu: {varForPlot}<br>"
        dane = f"""
            <p1> Funkjca wybarana poprawnie: {funkcja}</p1><br>
            <p1> Temp. do obliczeń: {str(tempObliczen)}<br>
            <p1> Ciśnienie do obliczeń: {str(cisnObliczen)}<br>
            <p1> Zakres min dla wykresu: {str(zakresMin)}<br>
            <p1> Zakres max dla wykresu: {str(zakresMax)}<br>
            <p1> Zmienna dla wykresu: {varForPlot}<br>
        """
        steam_table = XSteam(XSteam.UNIT_SYSTEM_MKS) #to jest złe miejsce na tworzenie obiektu steam_table bo za każdym razem jak się 
        # coś na stronie odświeży to będzie wykonywane. Docelowo ta linia powinna się tylko raz uruchamiać jak startuje strona /tablice_parowe
        uf_tsat_p = np.frompyfunc(steam_table.tsat_p,1,1)
        uf_hV_p = np.frompyfunc(steam_table.hV_p, 1, 1)
        uf_h_pt = np.frompyfunc(steam_table.h_pt,2,1)
        uf_hV_t = np.frompyfunc(steam_table.hV_t,1,1)
        uf_rho_pt = np.frompyfunc(steam_table.rho_pt,2,1) # jak powyżej - ten fragment też powinnien wykonywać się tylko raz
        x = np.arange(zakresMin, zakresMax, 0.1)
        plt.figure()
        plt.subplot(1,1,1)
        if funkcja == "tsat_p":
            y = uf_tsat_p(x)
            plt.title("Temperatura pary nasyconej w funkcji ciśnienia")
            plt.xlabel("bar abs.")
            plt.ylabel("\N{DEGREE SIGN}C")
        elif funkcja == "hV_p":
            y = uf_hV_p(x)
            plt.title("Entalpia pary nasyconej w funkcji ciśnienia (abs)")
            plt.xlabel("bar abs.")
            plt.ylabel("J")
        elif funkcja == "hV_t":
            y = uf_hV_t(x)
        elif funkcja == "h_pt":
            if varForPlot == "selectedPres":
                y = uf_h_pt(x,tempObliczen)
            elif varForPlot == "selectedTemp":
                y = uf_h_pt(cisnObliczen,x)
            else:
                y = np.ones(len(x))
        elif funkcja == "rho_pt":
            if varForPlot == "selectedPres":
                y = uf_rho_pt(x,tempObliczen)
            elif varForPlot == "selectedTemp":
                y = uf_rho_pt(cisnObliczen,x)
            else:
                y = np.ones(len(x))
        
        plt.plot(x,y)
        html_fig = mpld3.fig_to_html(plt.gcf())
            
        

        return steam_function+value+selectForPlot+hasiok+dane+html_fig+licznik
    ## wprowadzenie danych do obliczeń. W zależności od tego która funkcja została wybrana niektóre pola muszą zniknąć albo być nieaktywne (POST)
    # odebranie wprowadzonych danych
    # wyświetlenie wykresów

import xSteamIndex

funkcjeDict = xSteamIndex.index()

@app.route('/tablice_parowe_jinja', methods=['GET', 'POST'])
def tablice_parowe_jinja():
    global funkcjeDict, globalnyLicznik, funkcja, varForPlot, tempObliczen, cisnObliczen, zakresMin, zakresMax
    ## wybór funkcji - popup menue (POST)
    print(f"pracuje :) {globalnyLicznik}")
    globalnyLicznik += 1
    licznik = f"<br><p1> naliczyłem: {globalnyLicznik}; Metoda: {request.method}</p1>"
    input_p, input_t = 'disabled', 'disabled'
    steam_table = XSteam(XSteam.UNIT_SYSTEM_MKS) #to jest złe miejsce na tworzenie obiektu steam_table bo za każdym razem jak się 
    # coś na stronie odświeży to będzie wykonywane. Docelowo ta linia powinna się tylko raz uruchamiać jak startuje strona /tablice_parowe
            # niepotrzebny fragment kodu: zrobiłem to dynamicznie :)
            # uf_tsat_p = np.frompyfunc(steam_table.tsat_p,1,1)
            # uf_hV_p = np.frompyfunc(steam_table.hV_p, 1, 1)
            # uf_h_pt = np.frompyfunc(steam_table.h_pt,2,1)
            # uf_hV_t = np.frompyfunc(steam_table.hV_t,1,1)
            # uf_rho_pt = np.frompyfunc(steam_table.rho_pt,2,1) # jak powyżej - ten fragment też powinnien wykonywać się tylko raz
    formMethod = request.method

    if request.method == 'GET':
        # first start of app
        if funkcja == '' or None:
            funkcja = 'tsat_p'
        flash(f"Metoda: {formMethod}; plik: from_empty.html; licznik: {globalnyLicznik} ")
        # form_empty_path = os.path.join("\Templates", "form_empty.html")
        # print(form_empty_path)
        return render_template("form_empty.html", globalnyLicznik=globalnyLicznik, funkcja = funkcja, tempObliczen=tempObliczen, formMethod=formMethod, cisnObliczen=cisnObliczen, zakresMin=zakresMin, zakresMax=zakresMax, funkcjeDict=funkcjeDict, inputVar=inputVar)
    
    elif request.method == 'POST':
        flash(f"Metoda: {formMethod}; plik: from_filled.html; licznik: {globalnyLicznik} ")
        if "function" in request.form and request.form["function"] != None:
            if funkcja != request.form.get("function"): 
                # deleting indicator varForPlot
                for v in inputVar:
                    inputVar[v].varForPlot = False
                varForPlot = '' 
            # reading name of new selected function
            funkcja = request.form.get("function")
            # for function with only 1 input variable
            if funkcjeDict[funkcja].argsNr == 1: 
                varForPlot = funkcjeDict[funkcja].args[0]
                inputVar[funkcjeDict[funkcja].args[0]].varForPlot
        # read value from form; number of variable depends on selected function (from 0 to 2)
        for element in inputVar:    
            if inputVar[element].abbrev in request.form and inputVar[element].abbrev != None:
                inputVar[element].value = float(request.form.get(inputVar[element].abbrev))

        if "zakres_min" in request.form and request.form["zakres_min"] != None:
            zakresMin = float(request.form.get("zakres_min"))
        if "zakres_max" in request.form and request.form["zakres_max"] != None:
            zakresMax = float(request.form.get("zakres_max"))
        if "varForPlot" in request.form and request.form["varForPlot"] != None:
            varForPlot = request.form.get("varForPlot")
            for v in inputVar:
                    inputVar[v].varForPlot = False
            inputVar[request.form.get("varForPlot")].varForPlot = True

        if abs(zakresMax - zakresMin) > 0:
            x = np.arange(zakresMin, zakresMax, 0.1)
        else:
            x = 0

        plt.figure()
        plt.subplot(1,1,1)
        temp = funkcjeDict[funkcja].comment.split("Arg")
        plt.title(f"{ temp[0]}")
        temp = funkcjeDict[funkcja].comment.split("Returns:")
        plt.xlabel(f"{varForPlot} []")
        if varForPlot in inputVar:
            plt.xlabel(f"{ varForPlot} [{inputVar[varForPlot].unit}]")
        # print(f"{varForPlot}, {len(varForPlot), type(varForPlot)}")
        # print(inputVar[varForPlot].abbrev)
        temp = funkcja.split('_')[0] if funkcja.split('_')[0][-1].islower() else funkcja.split('_')[0][:-1]
        if temp in outputVar:
            plt.ylabel(f"{ temp} [{outputVar[temp].unit}]")
        else: 
            plt.ylabel(f"{ temp}")
        # if funkcja == "tsat_p":
        #     # y = uf_tsat_p(x)
        #     plt.title("Temperatura pary nasyconej w funkcji ciśnienia")
        #     plt.xlabel("bar abs.")
        #     plt.ylabel("\N{DEGREE SIGN}C")
        # elif funkcja == "hV_p":
        #     # y = uf_hV_p(x)
        #     plt.title("Entalpia pary nasyconej w funkcji ciśnienia (abs)")
        #     plt.xlabel("bar abs.")
        #     plt.ylabel("J")
        # elif funkcja == "hV_t":
        #     pass
        #     # y = uf_hV_t(x)
        # elif funkcja == "h_pt":
        #     if varForPlot == "selectedPres":
        #         # y = uf_h_pt(x,tempObliczen)
        #         pass
        #     elif varForPlot == "selectedTemp":
        #         # y = uf_h_pt(cisnObliczen,x)
        #         pass
        #     else:
        #         y = np.ones(len(x))
        # elif funkcja == "rho_pt":
        #     if varForPlot == "selectedPres":
        #         # y = uf_rho_pt(x,tempObliczen)
        #         pass
        #     elif varForPlot == "selectedTemp":
        #         # y = uf_rho_pt(cisnObliczen,x)
        #         pass
        #     else:
        #         y = np.ones(len(x))
        functionUfun = np.frompyfunc(getattr(steam_table, funkcja), funkcjeDict[funkcja].argsNr, 1)
        if funkcjeDict[funkcja].argsNr == 1:
            y = functionUfun(x)
        elif funkcjeDict[funkcja].argsNr == 2:
            if inputVar[funkcjeDict[funkcja].args[0]].varForPlot:
                y = functionUfun(x, inputVar[funkcjeDict[funkcja].args[1]].value)
            elif inputVar[funkcjeDict[funkcja].args[1]].varForPlot:
                y = functionUfun( inputVar[funkcjeDict[funkcja].args[0]].value, x)
            # else:
            #     y = np.ones(len(x))
        elif funkcjeDict[funkcja].argsNr == 0:
            y = np.zeros(len(x))*functionUfun()
        else:
            y = x

        if funkcjeDict[funkcja].argsNr in (1,2) and varForPlot in inputVar:
            plt.plot(x,y)
            html_fig = mpld3.fig_to_html(plt.gcf())
        elif funkcjeDict[funkcja].argsNr == 0:
            html_fig = f"<h2> Constant: {functionUfun()} </h2>"
        else:
            html_fig = f"<h2> Something went wrong :( </h2>"

        
        flash(f"<strong> Selected function - {funkcja}</strong><br> {funkcjeDict[funkcja].comment}")
        form_filled_path = os.path.join("Templates", "form_filled.html")
        
        return render_template("form_filled.html", globalnyLicznik=globalnyLicznik, funkcja=funkcja, \
                varForPlot=varForPlot, tempObliczen=tempObliczen, cisnObliczen=cisnObliczen,\
                 zakresMin=zakresMin, zakresMax=zakresMax, formMethod=formMethod,\
                funkcjeDict=funkcjeDict, inputVar=inputVar, html_fig=html_fig )
    else:
        flash(f"Metoda: {formMethod}; plik: from_empty.html; licznik: {globalnyLicznik} ")
        return render_template("form_empty.html",globalnyLicznik=globalnyLicznik, \
        tempObliczen=tempObliczen, formMethod=formMethod, cisnObliczen=cisnObliczen,\
              zakresMin=zakresMin, zakresMax=zakresMax, funkcjeDict=funkcjeDict, inputVar=inputVar)
    ## zbudować klasę która będzie zawierała informacje o funkcji z tab. parowej
    # str: nazwa fukcji
    # int: iloś arg
    # dict: nazwy argumentów {"t":"temperature", "p":"pressure", "rho": "density", "h": "enthalpy", "s":"entrophy"}
    # wygenerować listę zawierającą klasy opisujące funkcje term.



# Tylko na serwerach deweloperskich!
if app.debug:
    app.wsgi_app = DebuggedApplication(app.wsgi_app, True)





if __name__ == '__main__':
    app.run(debug=True)
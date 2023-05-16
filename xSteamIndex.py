
from pyXSteam.XSteam import XSteam
import inspect


class xSteamFuncInfo:
    def __init__(self,name):
        self.name = name
        self.args = []
        self.argspec = inspect.getfullargspec(getattr(XSteam, name))
        self.argsNr = len(self.argspec.args)-1
        self.args = self.argspec.args[1:]
        self.comment = getattr(XSteam, name).__doc__
        
    # def __str__(self):
    #     print(f"Function {self.name} has {self.argsNr} arguments (self not included): {self.args}")
    def args_nr(self):
        return self.argsNr
    def args_name(self):
        return self.args
    
def index():
    # uzyskaj listę nazw funkcji w klasie
    function_names = [func for func in dir(XSteam) if callable(getattr(XSteam, func)) and not func.startswith("__")]
    functionList = {}
    # iteruj po nazwach funkcji i wyświetl informacje o liczbie argumentów
    for name in function_names:
        funcTemp = xSteamFuncInfo(name)
        functionList.update({name:funcTemp})
    return functionList



if __name__ == '__main__':
    for k,v in index().items():
        print(f"Funkcja {k} ma {v.argsNr} \
              argumentów: {v.args}")
        print(v.comment)
    print(f"ROZMIAR LISTY: {len(index())}")



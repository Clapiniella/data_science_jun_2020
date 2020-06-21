import time

var1 = "2"
var2 = 3

def hola_y_adios():
    """ Muestra la palabra 'hola' y, un segundo más tarde, muestra 'adiós's por pantalla"""
    print("hola")
    time.sleep(1)  # Con esta línea obligamos a python a esperar 1 segundo.
    print("adiós")
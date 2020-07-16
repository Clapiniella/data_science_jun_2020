print("-----------")
print("Ejecución de 'a'")

def x():
    print("__name__ de 'a':")
    print(__name__)
    print("Estoy en el archivo 'a'")
    
print("Fin de ejecución de 'a'")
print("-----------")


if __name__ == "__main__":
    print("__name__ de a cumple condición")
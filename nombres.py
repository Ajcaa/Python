#Ejercicio 7
#Dado el diccionario que almacena la talla de algunas personas {'Marcelo': 1.80, 'José':1.50, 'Oscar':1.70, 'Jorge': 1.40}, 
# escriba un programa que dada una talla por el usuario imprima el nombre.


dict = {"1.80": "Marcelo", '1.50':"José", '1.70':"Oscar", '1.40': "Jorge"}


talla = input("Elija un talla para saber a quien pertenece: ").lower()
while talla not in ("1.80", "1.50", "1.70", "1.40"):
    talla = input("Tiene que colocar una opcion valida: ")

if talla == "1.80": 
    x = dict.get("1.80")
    print(x)
if talla == "1.50": 
    x = dict.get("1.50")
    print(x)
if talla == "1.70": 
    x = dict.get("1.70")
    print(x)
if talla == "1.40": 
    x = dict.get("1.40")
    print(x)

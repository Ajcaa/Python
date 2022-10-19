#Ejercicio 6
#Dado el diccionario que almacena la talla de algunas personas {'Marcelo': 1.80, 'José':1.50, 'Oscar':1.70, 'Jorge': 1.40}
# , escriba un programa que dado un nombre ingresado por el usuario imprime la talla.





dict = {'Marcelo': "1.80", 'José':"1.50", 'Oscar':"1.70", 'Jorge': "1.40"}


nombre = input("Elija un talla para saber a quien pertenece: ").lower()
while nombre not in ("marcelo", "jose", "oscar", "jorge"):
    nombre = input("Tiene que colocar una opcion valida: ").lower()

if nombre == "marcelo": 
    x = dict.get("Marcelo")
    print(x)
if nombre == "jose": 
    x = dict.get("José")
    print(x)
if nombre == "oscar": 
    x = dict.get("Oscar")
    print(x)
if nombre == "jorge": 
    x = dict.get("Jorge")
    print(x)
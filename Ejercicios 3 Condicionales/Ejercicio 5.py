#Ejercicio 5 Pedir lado y alto de un cuadrilátero y decir si es cuadrado o rectángulo by Valerie Sanchez 17-sism-1-063

lc=float(input("Introduzca el lado del cuadrilatero: "))
hc=float(input("Introduzca el alto del cuadrilatero: "))

suma1 = lc+hc

if lc < hc:
    print("Es rectangulo")
else:
    print("Es cuadrado")
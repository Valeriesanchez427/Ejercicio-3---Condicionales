#Ejercicio 3 Pedir tres números por teclado e imprimir el mayor de ellos solamente By Valerie Sanchez 17-sism-1-063

A=int(input("ingrese un numero\n"))
B=int(input("ingrese otro numero\n"))
C=int(input("ingrese un nuemero\n"))

if(A > B and A > C):
 print("El numero mayor es " + str(A))

else:
 if(B > A and B > C):
  print("El numero mayor es " + str(B))
  
 else:
  print("El numero mayor es " + str(C))
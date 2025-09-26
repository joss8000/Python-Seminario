dias=int(input("Ingrese un día (del 1 al 7): "))
if dias==1:
    print("Domingo")
elif dias==2:
    print ("Lunes")
elif dias==3:
    print("Martes")
elif dias==4:
    print("Miércoles")
elif dias==5:
    print("Jueves")
elif dias==6:
    print("Viernes")
elif dias==7:
    print("Sábado")
else:
    print("Error.")

cadena=input("Ingresar un caracter:")
print(f"lo ingresado es: {cadena}")
cadena2=int(input("Version?: "))
print(f"la version es: {cadena2}")
n1=90
n2=9.99
print("suma de valores: "n1+n2)
x=90
resultado=x-n1
print("resta de valores: "resultado)

numero=int(input("Ingrese un número: "))
if numero>0:
    print("El número es positivo.")
elif numero<0:
    print("El número es negativo.")
else:
    print("El número es cero.")

print("Fin del programa")
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
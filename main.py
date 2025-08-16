import random

# variables
caracteres_simples = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
caracteres_complejos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':\",./<>?`~"# solicitud

# Usar un bucle while para pedir la opción hasta que sea válida
opcion_valida = False

while not opcion_valida:
    opcion_dificultad = input("Elige la dificultad (1 = simple, 2 = compleja): ")

    if opcion_dificultad == "1":
        caracteres = caracteres_simples
        opcion_valida = True
    elif opcion_dificultad == "2":
        caracteres = caracteres_complejos
        opcion_valida = True
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")


#cliclo principal
longitud = int(input("Ingrese el tamanio de su contasenia: "))

contrasena = ""
for i in range(longitud):
    contrasena += random.choice(caracteres)


print(contrasena)
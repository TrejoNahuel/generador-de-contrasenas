import random

# --- Definición de variables y caracteres ---
# Creamos variables con los sets de caracteres para cada tipo de contraseña.
caracteres_simples = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
caracteres_complejos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':\",./<>?`~"

# --- Lógica de la elección de dificultad ---
# Usamos un bucle 'while' para pedir una opción hasta que sea válida.
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

# --- Lógica de la construcción de la contraseña ---
# Pedimos la longitud al usuario.
longitud = int(input("Ingrese el tamaño de su contraseña: "))

# Creamos una variable vacía para guardar la contraseña.
contrasena = ""

# Usamos un bucle 'for' para construir la contraseña carácter por carácter.
for i in range(longitud):
    contrasena += random.choice(caracteres)

# --- Mostrar el resultado ---
# Imprimimos la contraseña final.
print("\n¡Tu nueva contraseña es!")
print(contrasena)
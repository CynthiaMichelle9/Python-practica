import string
import random
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
            "password": random_pass()
        }
    return users_dictionary

lower_character = string.ascii_lowercase
upper_character = string.ascii_uppercase
numbers_character = string.digits

def random_pass():
    password = ""
    lower_part = ""
    upper_part = ""
    number_part = ""
    
    for _ in range(random.randint(5, 15)):
        lower_part = lower_part + random.choice(lower_character)
    
    for _ in range(random.randint(1, 5)):
        upper_part = upper_part + random.choice(upper_character)
    
    for _ in range(random.randint(3, 5)):
        number_part = number_part + random.choice(numbers_character)
    password = lower_part + upper_part + number_part
    return password

print(create_users(users_names_list))

# Cada cuenta debe guardarse en una nueva variable con su respectiva contraseña.

# Por cada cuenta debe pedir un número telefónico para contactarse.

# El programa no terminará de preguntar por los números hasta que todas las organizaciones tengan un número de contacto asignado.

#El programa debe verificar que el número telefónico tenga 8 dígitos numéricos.

#Se debe guardar como un string
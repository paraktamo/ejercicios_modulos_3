# verificacion.py: contiene funciones para verificar si la temperatura es adecuada.
"""
Crear una función es_temperatura_segura(temp) que devuelva True 
si la temperatura está entre -20 y 5 grados (inclusive).
Crear una función mostrar_estado(temp) que imprima si la temperatura 
es segura o peligrosa.

"""

def es_temperatura_segura(temp):
    return -20 <= temp <= 5
    
def mostrar_estado(segura):
    if segura:
        print("La temperatura es segura.")
    else:
        print("La temperatura es peligrosa.")

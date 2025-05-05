# registro.py: contiene funciones para registrar temperaturas
"""
Crear una función pedir_temperatura() que pida al usuario ingresar
 una temperatura (número entero) y verifique que esté entre -100 y 100 
 inclusive. Si el número no está en ese rango, se debe mostrar un mensaje 
 de error y volver a pedirlo.
No se requiere validar si un número es un entero, vamos a dar por válido 
que el usuario siempre ingresa un número de ese tipo.
Crear una función mostrar_temperatura(temp) que imprima la temperatura 
ingresada con un mensaje apropiado.

"""


def mostrar_temperatura(temp: int) -> int:
    """
    Recibe como param la temperatura ingresada y devuelve la misma.
    Se encarga de informar la temperatura que se ingresó.
    """
    print(f"La temperatura ingresada es: {temp}℃")
    return temp


def pedir_temperatura()-> int:
    """
    Es llamada incialmente en main.py, no recibe param, retorna la temperatura.
    Es una instancia de verificacion si la temperatura esta entre los valores
    aceptados.
    """
    temperature = int(input("Ingrese una temperatura (entre -100 y 100): "))

    if temperature > 100 or temperature < -100:
        print("Error: la temperatura debe estar entre -100 y 100.")
        # return pedir_temperatura()
    else:
        # mostrar_temperatura(temperature)
        return temperature


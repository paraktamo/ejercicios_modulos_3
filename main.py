"""
Importar las funciones necesarias de ambos módulos.
Usar un bucle para pedir 3 temperaturas distintas.
Por cada temperatura:
- Mostrarla.
- Verificar si es segura o peligrosa.
- Mostrar el estado correspondiente.

Ingrese una temperatura (entre -100 y 100): 150
Error: la temperatura debe estar entre -100 y 100.
Ingrese una temperatura (entre -100 y 100): - 25
La temperatura ingresada es: - 25℃
La temperatura es peligrosa.
- Ingrese una temperatura (entre -100 y 100): 0
- La temperatura ingresada es: 0°C
- La temperatura es segura.

"""
from control_temperatura.registro import pedir_temperatura as p_temp, mostrar_temperatura as m_temp
from control_temperatura.verificacion import es_temperatura_segura as e_t_segura, mostrar_estado as m_estado

for i in range(3):
    temp = p_temp()
    if temp != None:
        m_temp(temp)
        resultado = e_t_segura(temp)
        m_estado(resultado)

''' Carro Bluetooth con Raspberry Pi Pico W
Autor: Daniel Hernnadez Hernandez - 10002142
FCQeI Ing. Electrica - Electronica
Servicio Social abril-septiembre 2024
'''
#Librerias de configuracion
from machine import Pin,PWM # Pines a utilizar
from time import sleep # Tiempo 
import bluetooth # Modulo bluetooth
from ble_simple_peripheral import BLESimplePeripheral # Configuracion adicional del modulo

# Objeto para la configuración de BLE
ble = bluetooth.BLE()

# Instancia para el objeto anterior
sp = BLESimplePeripheral(ble)

#Configuración de motor izquierdo
ina = PWM(Pin(15)) # Cable Azul
in1 = Pin(14,Pin.OUT) # Cable Naranja
in2 = Pin(13,Pin.OUT) # Cable Verde
ina.freq(1000)
ina.duty_u16(65535)

#Configuración de motor dereho
inb = PWM(Pin(16)) # Cable Blanco
in3 = Pin(18,Pin.OUT) # Cable Cafe
in4 = Pin(17,Pin.OUT) # Cable Gris
inb.freq(1000)
inb.duty_u16(65535)

#Configuración de Faros
led_blanco = Pin(2,Pin.OUT)
led_blanco.off()
led_rojo = Pin(12,Pin.OUT)
led_rojo.off()

#Función a llamar para el programa principal
def auto (dato):
    print("Dato recibido: ", dato)  # Imprime el dato recibido
#Cada uno de los valores (b'instruccion') deberan ser configurados en la app
    if dato == b'Adelante':
        in1.low()
        in2.high()
        in3.high()
        in4.low()
        sleep(0.1)
        in1.low()
        in2.low()
        in3.low()
        in4.low()
        
    elif dato == b'Atras':
        in1.high()
        in2.low()
        in3.low()
        in4.high()
        sleep(0.1)
        in1.low()
        in2.low()
        in3.low()
        in4.low()

    elif dato == b'Derecha':
        in1.low()
        in2.high()
        in3.low()
        in4.high()
        sleep(0.1)
        in1.low()
        in2.low()
        in3.low()
        in4.low()
        
    elif dato == b'Izquierda':
        in1.high()
        in2.low()
        in3.high()
        in4.low()
        sleep(0.1)
        in1.low()
        in2.low()
        in3.low()
        in4.low()
    # Encendido de Luz Frontal
    elif dato == b'1':
        dato = int(dato)
        if dato == led_blanco.value():
            led_blanco.low()
        else:
            led_blanco.high()
     # Encendido Luz Tracera       
    elif dato == b'0':
        dato = int(dato)
        if dato == led_rojo.value():
            led_rojo.high()
        else:
            led_rojo.low()
    # Carro en stop
    else:
        in1.low()
        in2.low()
        in3.low()
        in4.low()
        
#Código principal
while True:
    if sp.is_connected():  # Revisa el estado de conexión
        sp.on_write(auto)  # Llama la funcion a realizar
    
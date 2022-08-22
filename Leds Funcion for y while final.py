from machine import Pin
import utime

led1=Pin(15,Pin.OUT)
led2=Pin(4,Pin.OUT)
led3=Pin(17,Pin.OUT)
led4=Pin(18,Pin.OUT)
todos =[led1, led2, led3, led4]

def derecha():
    for elem in todos:
        elem.value(1)
        utime.sleep_ms(200)
        elem.value(0)
        utime.sleep_ms(200)
def izquierda():
    for elem in reversed(todos):
        elem.value(1)
        utime.sleep(0.2)
        elem.value(0)
        utime.sleep(0.2)
while True:
    derecha()
    #opcional izquierda()
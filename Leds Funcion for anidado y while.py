from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau

ledb=pin(4,pin.OUT)
ledc=pin(17,pin.OUT)
leda=pin(15,pin.OUT)
ledd=pin(18,pin.OUT)

todos=[leda, ledb, ledc, ledd]

def derecha ():
    for i in todos:
        for j in range(2):
            i.value(not i.value())
            pausam(150)
def izquierda():
    for i in todos:
        for j in range(2):
            i.value(not i.value())
            pausam(300)
while True:
    izquierda()
    #Opcional izquierda()
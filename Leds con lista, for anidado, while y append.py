from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau

puerto=[15, 4, 17, 18]
tds=[]
for i in puerto:
    tds.append (pin(i,pin.OUT))
print(tds)

def derecha():
    for i in tds:
        for j in range(2):
            i.value(not i.value())
        pausam(250)
def izquierda():
    for i in tds:
        for j in range(2):
            i.value(not i.value())
        pausam(250)
while True:
    izquierda()
    #Opcional izquierda()
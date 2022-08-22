from machine import Pin as pin
from utime import sleep, sleep_ms

led1=pin(15,pin.OUT)
led2=pin(4,pin.OUT)
led3=pin(17,pin.OUT)
led4=pin(18,pin.OUT)

pausa=0.2

while True:
    led1.value(1)
    sleep(pausa)
    led1.value(0)
    sleep(pausa)
    led2.value(1)
    sleep(pausa)
    led2.value(0)
    sleep(pausa)
    led3.value(1)
    sleep(pausa)
    led3.value(0)
    sleep(pausa)
    led4.value(1)
    sleep(pausa)
    led4.value(0)
    sleep(pausa)
    


from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau

leda=pin(15,pin.OUT)
ledb=pin(4,pin.OUT)
ledc=pin(17,pin.OUT)
ledd=pin(18,pin.OUT)

def print_led(a, b, c, d):
    leda.value(a)
    ledb.value(b)
    ledc.value(c)
    ledd.value(d)
    pausam(200)
    
while True:
    print_led(0,0,0,1)
    print_led(0,0,1,0)
    print_led(0,1,0,0)
    print_led(1,0,0,0)
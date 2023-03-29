from machine import Pin, Timer # MicroPython
from time import sleep

led = Pin(25, Pin.OUT) # Built-in LED on top
print("Running...")


led.value(0) # BLUE
sleep(2)

led.value(1) # GREEN
sleep(2)


while(True):    

    led.value(0) # BLUE
    sleep(1)

    led.value(1) # GREEN
    sleep(1)



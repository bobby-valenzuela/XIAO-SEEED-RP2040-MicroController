from machine import Pin, Timer # MicroPython
from time import sleep
import neopixel 	# RGB Functionality

# IR Sensor
prox_sensor = Pin(26, Pin.IN) 			


### USER RGBs (top right of xiao)
blue_led = Pin(25, Pin.OUT,value=None) 	# Built-in LED on top [BLUE]
red_led = Pin(16, Pin.OUT,value=None) 	# Built-in LED on top [GREEN]
green_led = Pin(17, Pin.OUT,value=None) # Built-in LED on top [RED]
usr_leds = { 'blue_led':blue_led, 'red_led':red_led, 'green_led':green_led}

from usr_led import *


### Main RBG (bottom center of xiao)
num_pixels=1
rbg_pin=12 # NEOPIXEL Pin, uses P11 for pwr
np = neopixel.NeoPixel(machine.Pin(rbg_pin), num_pixels)
np_pwr = Pin(11, Pin.OUT,value=1) 	# Built-in LED on top [BLUE]

from neopixel_utils import *

# Set/display colour
# np[0] = red_quarter
# np.write()
# sleep(3)
# np_pwr.off()


def detected_obj():
    return 1 if prox_sensor.value() == 0 else 0


"""
===================================
MAIN PROGRAM START
===================================
"""

print("Running...")



while True:

    if detected_obj() == 0 :
        usr_led_off(usr_leds)
    else:
        print("DETECTED!")
        
        # Light up small usr leds
        usr_led_blue_high(usr_leds)
        
        # Blink main RGB LED
        led_pulse_hyper(np,'green')

    sleep(0.01)



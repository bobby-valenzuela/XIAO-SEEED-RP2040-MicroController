def usr_led_blue_high(usr_leds):
    usr_leds['green_led'].on()
    usr_leds['red_led'].off()
    usr_leds['blue_led'].off()

def usr_led_blue_low(usr_leds):
    usr_leds['green_led'].on()
    usr_leds['red_led'].on()
    usr_leds['blue_led'].off()

def usr_led_blue_red_high(usr_leds):
    usr_leds['green_led'].off()
    usr_leds['red_led'].off()
    usr_leds['blue_led'].off()

def usr_led_blue_red_low(usr_leds):
    usr_leds['green_led'].off()
    usr_leds['red_led'].on()
    usr_leds['blue_led'].off()

def usr_led_green(usr_leds):
    usr_leds['green_led'].on()
    usr_leds['red_led'].off()
    usr_leds['blue_led'].on()

def usr_led_green_red(usr_leds):
    usr_leds['green_led'].off()
    usr_leds['red_led'].off()
    usr_leds['blue_led'].on()

def usr_led_red(usr_leds):
    usr_leds['green_led'].off()
    usr_leds['red_led'].on()
    usr_leds['blue_led'].on()

def usr_led_off(usr_leds):
    # Only red usr_led shows (power)
    usr_leds['green_led'].on()
    usr_leds['red_led'].on()
    usr_leds['blue_led'].on() 

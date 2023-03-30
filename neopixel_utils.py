from time import sleep

# Define colours
red = (255, 0, 0) # set to red, full brightness
red_quarter = (64, 0, 0) # set to red, quarter brightness
red_half = (128, 0, 0) # set to red, half brightness

green = (0, 255, 0) # set to green
green_quarter = (0, 64, 0) # set to green, quarter brightness
green_half = (0, 128, 0) # set to green, half brightness

blue = (0, 0, 255)  # set to blue
blue_quarter = (0, 0, 64)  # set to blue, quarter brightness
blue_half = (0, 0, 128)  # set to blue, half brightness


def led_fade(np,color='red',direction='in',speed=0.003):
    
    if speed == 'hyper': speed = 0.0001
    if speed == 'fast': speed = 0.001
    if speed == 'slow': speed = 0.005
    
    if direction == 'out':
        values = reversed(range(255))
    else:
        values = range(255)
    
    red = green = blue = 0
    
    for i in values:
        
        if color.lower() == 'red': red = i
        if color.lower() == 'green': green = i
        if color.lower() == 'blue': blue = i
        
        np[0] = (red, green, blue)
        np.write()
        sleep(speed)

def led_pulse(np,color):
    led_fade(np,color)
    led_fade(np,color,direction='out')

def led_pulse_fast(np,color):
    led_fade(np,color,speed='fast')
    led_fade(np,color,direction='out',speed='fast')

def led_pulse_hyper(np,color):
    led_fade(np,color,speed='hyper')
    led_fade(np,color,direction='out',speed='hyper')
        
def led_pulse_slow(np,color):
    led_fade(np,color,speed='slow')
    led_fade(np,color,direction='out',speed='slow')
    

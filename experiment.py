import bluetooth
import time
from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
tree = LEDBoard(*range(2,28),pwm=True)

def reset():
  for led in tree:
    print "off"
    led.off()

def flicker():
 for led in tree:
    led.source_delay = 0.1
    led.source = random_values()

def isNikolajIn():
  result = bluetooth.lookup_name('94:65:2D:62:76:0C', timeout=5)
  if (result != None):
    print "Nikolaj: in"
    return True
  else:
    print "Nikolaj: out"
    return False

while True:
  if (isNikolajIn()):
    flicker()
  else:
    reset()
  time.sleep(5)

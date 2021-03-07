from sense_emu import SenseHat
from time import sleep

sense = SenseHat()
#sensor.low_light = True

#makeover time! Here is a Python list. It holds  collection of string values.

names = ["Codey" , "Meep" , "Freedy", "Voltria" , "Kat-Kat", "Kayley", "Joseph", "Alyssa", "Lateef"]

names.append("Lizardia")

sense.show_message(names[1])

#Colors:

r = (255, 0, 0 ) # RED color, stored in an another data structure called a tuple.
w = (255, 255, 255) #white is all colors maxed
k = (0, 0, 0) # black means zero amounts of red, green and blue
g = (0, 255, 0) #green
p = (255,162,207) #meep pink
b = (63, 181, 222) #meep blue

#define another color. Use one letter variable names to make it easy later

raspimon = [
k, k, k, k, k, k, k, k,
k, r, r, r, r, r, r, k,
k, r, k, k, k, k, r, k,
k, r, r, k, r, k, r, k,
k, r, k, k, k, k, r, k,
k, r, r, r, r, r, r, k,
k, k, r, k, r, k, k, k,
k, k, r, k, r, k, k, k
]
 
sense.set_pixels(raspimon)

#add a one-pixel mouth
  

sense.set_pixels(meep)
sleep(1.5)
sense.set_pixels(meep_facing_right)
sleep(1.0)
sense.set_pixels(meep_facing_left)
sleep(1.0)
sense.set_pixels(meep)
sleep(1.0)
sense.set_pixels(meep_mouth_open)
sleep(0.3)
sense.set_pixels(meep_mouth_closed)
sleep(0.3)
sense.set_pixels(meep_mouth_open)
sleep(0.3)
sense.set_pixels(meep_mouth_closed)
sleep(0.3)
sense.set_pixels(meep_mouth_open)
sleep(0.3)
sense.set_pixels(meep_mouth_closed)
sleep(0.3)
sense.set_pixels(meep_mouth_open)
sleep(0.3)
sense.set_pixels(meep_mouth_closed)
sleep(0.3)
sense.set_pixels(meep)
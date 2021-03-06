from sense_emu import SenseHat   #import the SenseHat object from the sense_hat library
from time import sleep

#this is how you load the sense object so you can use it in this script.
sense = SenseHat()

#creating variables to store RGB colors
p = (128, 0, 128) #pink
w = (255, 255, 255) #white
k = (0,0,0) #blank

text_colour=[255, 255, 0] 
back_colour=[ 0 ,0, 255]

egg = [p,p,p,p,p,p,p,p,
       p,p,p,w,w,p,p,p,
       p,p,w,w,w,w,p,p,
       p,p,w,w,w,w,p,p,
       p,p,w,w,w,w,p,p,
       p,p,w,w,w,w,p,p,
       p,p,p,w,w,p,p,p,
       p,p,p,p,p,p,p,p]
       
hatched = [k,k,k,k,k,k,k,k,
           k,k,k,p,p,p,k,k,
           k,k,p,p,p,p,p,k,
           k,k,p,k,p,k,p,k,
           k,k,p,w,p,w,p,k,
           k,k,k,p,p,p,k,k,
           k,k,k,p,p,p,k,k,
           k,k,p,p,k,p,p,k ]

#this is how you scroll a message
sense.show_message("I'm still an egg!")

#add more messages below. 


#sense.show_message("I love red!", text_colour=[255,0,0])

#the sense object has functions we can use: set_pixels. The value in the parentheses should be the egg.
sense.set_pixels(egg)
sleep(1.5)

sense.show_message("I’m ready to hatch soon!")
sense.set_pixels(hatched)
from sense_hat import SenseHat
from time import sleep

#below are simple print statments. 
#Any code between quotation marks are considered Strings, or text.

print("The FitnessGram Pacer test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter Pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal *boop*. A single lap should be completed each time you hear this sound *ding*. Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.")

#We can import other Python code to help us. Sleep is like a pause in the code.
#Change the value inside the sleep() function call to change the pause amount.
sleep(1) 

print("Let's get started!")

sleep(1.5)

print("what's your name?")

#input is used to get text input from a keyboard. We store it as a variable called name
#the \n forces a new line.
name = input("my name is: \n")

sleep(1)

#Use the name in a new print statement. You can combine strings with the + symbol.
print("Nice to meet you, " + name)

sleep(1)

print("I think you are ready to meet your Raspimon in Lab 2.")



 

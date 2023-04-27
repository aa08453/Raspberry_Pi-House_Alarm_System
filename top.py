#preamble
from gpiozero import LED
from gpiozero import Button
from gpiozero import DistanceSensor
from gpiozero import Buzzer
from gpiozero import PWMLED
from time import sleep
from signal import pause
from main_func import main

#gpio pinouts for 
R1 = LED(14)
R2 = LED(15)
R3 = LED(18)
R4 = LED(23)

#gpio pinouts for columns of keypad treated as buttons
C1 = Button(24)
C2 = Button(25)
C3 = Button(8)

sensor = DistanceSensor(echo=26, trigger=21) #gpio pins for the sensor,
buzzer = Buzzer(2) # gpio pin for buzzer

#gpio pinouts for a RGB LED where each pin sets one of the 3 colours
Blue = LED(11) 
Green = LED(9)
Red = LED(10)

global active
active = False

code = ""
password = "4567" #setting a random 4 digit passcode

#initializing the alarm system in inactive state
main(False)

pause()
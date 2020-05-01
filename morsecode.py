from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import time
RPi.GPIO.setmode(RPi.GPIO.BCM)

## hardware
led = LED(18)

## GUI DEFINITIONS ##
win = Tk()
win.title("Morse Code")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")
blinks = ''

## Event Functions
def dot():
    print('dot')
    led.on()
    time.sleep(0.25)
    led.off()
    time.sleep(0.25)
def dash():
    print('dash')
    led.on()
    time.sleep(0.55)
    led.off()
    time.sleep(0.55)

def morseCode(char):
    print(char);
    if(char == 'a'):
        dot()
        dash()
        
    elif(char == 'b'):
        dash()
        dot()
        dot()
        dot()
        
    elif(char == 'c'):
        dash()
        dot()
        dash()
        dot()
        
    elif(char == 'd'):
        dash()
        dot()
        dot()
        
    elif(char == 'e'):
        dot()

    elif(char =='f'):
        dot()
        dot()
        dash()
        dot()
        
    elif(char == 'g'):
        dash()
        dash()
        dot()
        
    elif(char == 'h'):
        dot()
        dot()
        dot()
        dot()
        
    elif(char == 'i'):
        dot()
        dot()
        
    elif(char == 'j'):
        dot()
        dash()
        dash()
        dash()
        
    elif(char == 'k'):
        dash()
        dot()
        dash()
        
        
    elif(char == 'l'):
        dot()
        dash()
        dot()
        dot()
        
        
    elif(char == 'm'):
        dash()
        dash()
        
    elif(char == 'n'):
        dash()
        dot()
        
    elif(char == 'o'):
        dash()
        dash()
        dash()
        
    elif(char == 'p'):
        dot()
        dash()
        dash()
        dot()
        
    elif(char == 'q'):
        dash()
        dash()
        dot()
        dash()  
        
    elif(char == 'r'):
        dot()
        dash()
        dot()
        
    elif(char == 's'):
        dot()
        dot()
        dot()
        
    elif(char == 't'):
        dash()
        
    elif(char == 'u'):
        dot()
        dot()
        dash()
        
    elif(char == 'v'):
        dot()
        dot()
        dot()
        dash()
        
    elif(char == 'w'):
        dot()
        dash()
        dash()
        
    elif(char == 'x'):
        dash()
        dot()
        dot()
        dash()
      
    
    elif(char == 'y'):
        dash()
        dot()
        dash()
        dash()
        
    elif(char == 'z'):
        dash()
        dash()
        dot()
        dot()
        
    else:
        print("Invalid character")
        

def letters(input):
    for l in input:
        morseCode(l);
        time.sleep(1);

def ledBlink():
    blinks = key.get()
    print("Morse code ", blinks) 
    letters(blinks.lower())

def close():
    RPi.GPIO.cleanup()
    win.destroy()

### WIDGETS ###
ledButton = Button(win, text = 'Enter a name or word', font = myFont, command = ledBlink, bg = 'bisque2', height = 1)
ledButton.grid(row=0,column=1)
key = Entry(win, font=myFont, width=12)
key.grid(row=0,column=0)
exitButton = Button(win, text='Exit', font=myFont, command=close,bg='red', height=1, width=6)
exitButton.grid(row=3,column=1, sticky=E)


win.protocol("WM_DELETE_WINDOW", close) 
win.mainloop()
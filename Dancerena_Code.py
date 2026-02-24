from machine import Pin, PWM
import time
import random

up = Pin(19, Pin.IN, Pin.PULL_UP)
down = Pin(34, Pin.IN, Pin.PULL_UP)
left = Pin(21, Pin.IN, Pin.PULL_UP)
right = Pin(18, Pin.IN, Pin.PULL_UP)


led_up = Pin(4, Pin.OUT)
led_down = Pin(14, Pin.OUT)
led_left = Pin(23, Pin.OUT)
led_right = Pin(13, Pin.OUT)

buzzer = PWM(Pin(32))
buzzer.duty_u16(2000)


C5 = 523
D5 = 587
E5 = 659
G4 = 392
A4 = 440
G5 = 784

while True:
    
    song = 0
    while song == 0:
        if up.value() == 0:
            song = 1
        elif down.value() == 0:
            song = 2
        elif right.value() == 0:
            song = 3
        elif left.value() == 0:
            song = 4
        time.sleep(0.05)
    time.sleep(0.5)

    
    wrong = 0
    while wrong == 0:
        pattern = [random.randint(1, 4) for i in range(5)]
        i = 0
        while i < 5 and wrong == 0:
            step = pattern[i]

         
            buzzer.duty_u16(2000)
            if song == 1:
                buzzer.freq(C5)
                time.sleep(0.15)
                buzzer.freq(E5)
                time.sleep(0.15)
                buzzer.freq(G5)
                time.sleep(0.25)
            elif song == 2:
                buzzer.freq(G4)
                time.sleep(0.25)
                buzzer.freq(A4)
                time.sleep(0.15)
                buzzer.freq(G4)
                time.sleep(0.25)
            elif song == 3:
                buzzer.freq(C5)
                time.sleep(0.1)
                buzzer.freq(C5)
                time.sleep(0.1)
                buzzer.freq(D5)
                time.sleep(0.1)
                buzzer.freq(E5)
                time.sleep(0.2)
            elif song == 4:
                buzzer.freq(E5)
                time.sleep(0.25)
                buzzer.freq(D5)
                time.sleep(0.2)
                buzzer.freq(C5)
                time.sleep(0.3)
            buzzer.duty_u16(0)

            
            led_up.value(step == 1)
            led_down.value(step == 2)
            led_left.value(step == 3)
            led_right.value(step == 4)
            time.sleep(0.4)
            led_up.value(0)
            led_down.value(0)
            led_left.value(0)
            led_right.value(0)
           
            pressed = 0
            while pressed == 0:
                if up.value() == 0:
                    if step == 1:
                        pressed = 1
                    else:
                        wrong = 1
                        pressed = 1
                elif down.value() == 0:
                    if step == 2:
                        pressed = 1
                    else:
                        wrong = 1
                        pressed = 1
                        
            
                elif left.value() == 0:
                    if step == 3:
                        pressed = 1
                    else:
                        wrong = 1
                        pressed = 1
                elif right.value() == 0:
                    if step == 4:
                        pressed = 1
                    else:
                        wrong = 1
                        pressed = 1
                time.sleep(0.01)
            i = i + 1

        
        if wrong == 1:
            buzzer.freq(200)
            buzzer.duty_u16(4000)
            time.sleep(0.5)
            buzzer.duty_u16(0)

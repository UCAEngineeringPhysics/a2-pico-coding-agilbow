from time import sleep
from machine import Pin, PWM, Timer

# SETUP
led = PWM(Pin(15))
led.freq(1000)
led.duty_u16(0)

button = Pin(14, Pin.IN, Pin.PULL_DOWN)


def mode_switch(pin):
    global modeValue
    modeValue += 1

button.irq(trigger=Pin.IRQ_FALLING, handler=mode_switch) 

modeValue = 0

dutyValue = 0
dutyIncrease = 655
dutyDecrease = 655

# LOOP
while True:
    if modeValue % 2 == 0:
        led.duty_u16(65535)
    else:
        dutyValue = 0
        for i in range(100):
            led.duty_u16(dutyValue)
            dutyValue = dutyValue + dutyIncrease
            sleep(1/100)
            if modeValue % 2 == 0:
                break
        for i in reversed(range(100)):
            led.duty_u16(dutyValue)
            dutyValue = dutyValue - dutyDecrease
            sleep(1/100)
            if modeValue % 2 == 0:
                break
            
            
            
            
            






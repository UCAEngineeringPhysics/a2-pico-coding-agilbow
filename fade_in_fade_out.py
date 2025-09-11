from time import sleep
from machine import Pin, PWM, Timer

#insert the pin number when making the circuit
LED = Pin(15, Pin.OUT)
pwm = PWM(LED)

#set the frequency
pwm.freq(1000)

#start the duty cycle at 0 so that it can be increased to max in 2 seconds
dutyValue = 0
pwm.duty_u16(dutyValue)

#set the increment for the duty cycle to increase by
dutyIncrease = 655

#set the increment for the duty cycle to decrease by
dutyDecrease = 655

#create while loop
while True:
    for i in range(100):
        pwm.duty_u16(dutyValue)
        dutyValue = dutyValue + dutyIncrease
        print(dutyValue)
        sleep(2/100)
    for i in reversed(range(100)):
        pwm.duty_u16(dutyValue)
        dutyValue = dutyValue - dutyIncrease
        print(dutyValue)
        sleep(1/100)
        



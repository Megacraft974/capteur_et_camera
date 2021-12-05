from gpiozero import PWMOutputDevice
from time import sleep
a = PWMOutputDevice(4)
b = PWMOutputDevice(2)
a.off()
a.on()
b.off()
while True:
    a.off()
    sleep(1)
    a.on()
    sleep(1)

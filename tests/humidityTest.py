import pigpio
from time import sleep
# this connects to the pigpio daemon which must be started first
pi = pigpio.pi()
# Pigpio DHT22 module should be in same folder as your program
import DHT22 



def read(pin):
	s = DHT22.sensor(pi, pin)
	s.trigger()
	sleep(1) # Necessary on faster Raspberry Pi's
	print('humidity: {:3.2f}'.format(s.humidity() / 1.))
	print('temperature: {:3.2f}'.format(s.temperature() / 1.))
	s.cancel()
for i in range(0,50):
	read(10) 
pi.stop()

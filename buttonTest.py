import RPi.GPIO as GPIO
import time,os,signal,sys
import subprocess
import multiprocessing

m1 = 5 #electric
l_btn = 0
r_btn = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(m1, GPIO.OUT)
GPIO.setup(14,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def goright():
	r_btn = GPIO.input(14)
	time.sleep(1)
	while(r_btn==0):
		time.sleep(0.1)
		r_btn = GPIO.input(14)
	
def goleft():
	l_btn = GPIO.input(15)
	time.sleep(1)
	while(l_btn==0):
		time.sleep(0.1)
		l_btn=GPIO.input(15)

GPIO.output(m1,GPIO.HIGH)
time.sleep(1)


while True:
	print('14')
	print(GPIO.input(14))
	print('15')
	print(GPIO.input(15))
	print('')
	time.sleep(0.5)

	#goright()
	#GPIO.output(m1,GPIO.LOW)
	#time.sleep(0.4)

	#goleft()
	#GPIO.output(m1.GPIO.HIGH)
	#time.sleep(0.4)
	
GPIO.cleanup()
	 

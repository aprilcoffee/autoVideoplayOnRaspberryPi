import RPi.GPIO as GPIO
import time,os,signal,sys
import subprocess
import multiprocessing

m1 = 5
m2 = 6
l_btn = 0
r_btn = 0
nowPlaying=0
wasPlaying=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(m1, GPIO.OUT)
GPIO.setup(m2, GPIO.OUT)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def goright():
	global nowPlaying
	global wasPlaying 
	wasPlaying = 0
	GPIO.output(m1,GPIO.LOW)
	GPIO.output(m2,GPIO.LOW)
	r_btn = GPIO.input(23)
	time.sleep(2)
	while(r_btn==0):
		GPIO.output(m1,GPIO.HIGH)
		GPIO.output(m2,GPIO.LOW)
		time.sleep(0.1)
		r_btn = GPIO.input(23)
	GPIO.output(m1,GPIO.LOW)
	GPIO.output(m2,GPIO.LOW)
	

def goleft():
	global nowPlaying
	global wasPlaying
	wasPlaying = 1
	GPIO.output(m1,GPIO.LOW)
	GPIO.output(m2,GPIO.LOW)
	l_btn = GPIO.input(24)
	time.sleep(2)
	while(l_btn==0):
		GPIO.output(m1,GPIO.LOW)
		GPIO.output(m2,GPIO.HIGH)
		time.sleep(0.1)
		l_btn=GPIO.input(24)
	GPIO.output(m1,GPIO.LOW)
	GPIO.output(m2,GPIO.LOW)
	
GPIO.output(m1,GPIO.LOW)
GPIO.output(m2,GPIO.LOW)
time.sleep(1)

proc1 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--aspect-mode','fill','tomotor2.mp4'])
print 'proc\'s pid = ',proc1.pid

while True:
	goright()
	nowPlaying = 1
	proc2 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--aspect-mode','fill','towheel2.mp4'])
	time.sleep(0.7)
	subprocess.call(['pkill','-P',str(proc1.pid)])	
	proc1.kill()
	print 'proc\'s pid = ',proc2.pid
	
	goleft()
	nowPlaying = 0
	proc1 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--aspect-mode','fill','tomotor2.mp4'])
	time.sleep(0.7)
	subprocess.call(['pkill','-P',str(proc2.pid)])
	proc2.kill()
	print 'proc\'s pid = ',proc1.pid
	
GPIO.cleanup()
	 

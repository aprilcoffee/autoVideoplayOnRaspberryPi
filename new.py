import RPi.GPIO as GPIO
import time,os,signal,sys
import subprocess
import multiprocessing

m1 = 18 #electric
l_btn = 0
r_btn = 0
nowPlaying = 0
wasPlaying = 0
playingFlag = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(m1, GPIO.OUT)
GPIO.setup(14,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def goright():
	global nowPlaying
	global wasPlaying 
	wasPlaying = 0
	#GPIO.output(m1,GPIO.LOW)
	r_btn = GPIO.input(14)
	time.sleep(1)
	while(r_btn==0):
	#	GPIO.output(m1,GPIO.HIGH)
		time.sleep(0.1)
		r_btn = GPIO.input(14)
	#GPIO.output(m1,GPIO.LOW)
	

def goleft():
	global nowPlaying
	global wasPlaying
	wasPlaying = 1
	#GPIO.output(m1,GPIO.LOW)
	l_btn = GPIO.input(15)
	time.sleep(1)
	while(l_btn==0):
	#	GPIO.output(m1,GPIO.HIGH)
		time.sleep(0.1)
		l_btn=GPIO.input(15)
	#GPIO.output(m1,GPIO.LOW)

GPIO.output(m1,GPIO.HIGH)
time.sleep(1)

proc1 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--aspect-mode','fill','asset/000.mp4'])
print 'proc\'s pid = ',proc1.pid

while True:
	global playingFlag
	goright()
	nowPlaying = 1
        if playingFlag == 1:
        	proc2 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--aspect-mode','fill','asset/001.mp4'])
        elif playingFlag == 2:
                proc2 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--aspect-mode','fill','asset/002.mp4'])
        elif playingFlag == 3:
                proc2 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--aspect-mode','fill','asset/003.mp4'])
        elif playingFlag == 4:
                proc2 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--aspect-mode','fill','asset/004.mp4'])
        elif playingFlag == 5:
                proc2 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--aspect-mode','fill','asset/005.mp4'])
        elif playingFlag == 6:
                proc2 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--aspect-mode','fill','asset/006.mp4'])
        elif playingFlag == 7:
                proc2 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--aspect-mode','fill','asset/007.mp4'])
        elif playingFlag == 8:
                proc2 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--aspect-mode','fill','asset/008.mp4'])
        elif playingFlag == 9:
                proc2 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--aspect-mode','fill','asset/009.mp4'])
        GPIO.output(m1,GPIO.LOW)
	time.sleep(0.5)
	subprocess.call(['pkill','-P',str(proc1.pid)])	
	proc1.kill()
	print 'proc\'s pid = ',proc2.pid
	
	goleft()
	print('HELLO')
	playingFlag += 1
	if playingFlag > 9:
		playingFlag = 1
	nowPlaying = 0
	print('ChangeSub')
	proc1 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--aspect-mode','fill','asset/000.mp4'])
	print('PlayVideo')
	GPIO.output(m1,GPIO.HIGH)
	time.sleep(0.5)
	subprocess.call(['pkill','-P',str(proc2.pid)])
	proc2.kill()
	print 'proc\'s pid = ',proc1.pid
	
GPIO.cleanup()
	 

import RPi.GPIO as GPIO
import time,os,signal,sys
import subprocess
import multiprocessing


GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

playingFlag = 1

def playA():
    btn = GPIO.input(21)
    print(btn)
    time.sleep(1)
    while(btn==0):
        time.sleep(0.1)
        btn = GPIO.input(21)
def playB():
    btn = GPIO.input(21)
    print(btn)
    time.sleep(1)
    while(btn==1):
        time.sleep(0.1)
        btn=GPIO.input(21)


proc1 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--aspect-mode','fill','/home/pi/off.mp4'])

while True:
    playA()
    proc2 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--aspect-mode','fill','/home/pi/on.mp4'])
    time.sleep(1.35)
    subprocess.call(['pkill','-P',str(proc1.pid)])
    proc1.kill()

    playB()
    proc1 = subprocess.Popen(args=['omxplayer','--no-osd','--loop','-b','--aspect-mode','fill','/home/pi/off.mp4'])
    time.sleep(1.35)
    subprocess.call(['pkill','-P',str(proc2.pid)])
    proc2.kill()

GPIO.cleanup()

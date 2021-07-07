#!/bin/bash

DIR=/media/pi/
sleep 5
while true; do
#if pgrep omxplayer > /dev/null
if false;
then
	echo "running"
else 
	for d in `ls $DIR | grep ""` 
	do
		echo "$d"
		FILES="$DIR${d}"



		for f in `ls $FILES | grep ".mp4$\|.mov$\|.mp3$\|.wav$"`
		do	
			playDir="$FILES"
			vids="$f"
			echo "$f"
		done
	done
	omxplayer -o local --no-keys --loop "$playDir/${vids}" &
	break
	
fi
done

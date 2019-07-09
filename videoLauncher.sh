#!/bin/bash

DIR=/media/pi/

while true; do
if pgrep omxplayer > /dev/null
then
	echo "running"
else 
	for d in `ls $DIR | grep ""` 
	do
		echo "$d"
		FILES="$DIR${d}"



		for f in `ls $FILES | grep ".mp4$\|.mov$"`
		do	
			playDir="$FILES"
			vids="$f"
			echo "$f"
		done
	done
	omxplayer -o both --no-osd --loop -b --aspect-mode fill "$playDir/${vids}"
	
fi
done

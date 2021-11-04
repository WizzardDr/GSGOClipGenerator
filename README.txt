HOW TO USE - to generate 1s lossless kill clips.

Requirements:
Python (https://www.python.org/downloads/)
NodeJs (https://nodejs.org/en/download/)
OBS    (https://obsproject.com/download)


Setup:
========================================
1.OBS Settings (settings button bottem right)
a. Set recording      Settings>Output>Recording Quality>(Lossless Qualitym Tremendously Large File Size)
b. Recording Path     Settings>Output>Recording Path <Set it to the same root location as this readme>
c. Record Hotkey      Settings>Hotkeys>Start Recording* <I used F8>
		                       Stop Recording* <I used F9>
d. FPS                Settings>Video>FPS Values: 60

2.Copy file named: gamestate_integration_yourservicenamehere.cfg  into \Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg

e.g.steam libary location, mine is(E:\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg)

========================================



Recording:
=======================================
1. Run the CSGOStats.js applicaton using node.
   Option A. Start a command promt and navigate to the file (in it current location), then run node CSGOStats.js
   Optoin B. Right click the .js file and open with > Choose another app> more apps > "C:\Program Files\nodejs\node.exe" (reccomended)
             (Option B will allow you to run the node application in future by doubble clicking it.)

2. Launch OBS, (dont start recording yet)
3. Join a CSGO session.
4. Tab to the node comand prompt window.
5. Once a stream of numbers and data starts, Press record using your hot key (i.e. f8) ENSURING THE TERMINAL IS IN THE RECORDING AREA!
6. Play a round. (I recomend only playing one round as the recording is huge and will be 35gb+) but the system now supports endless rounds.
7. Access the menu to trigger a save of the game kill data. "Not in Game..." in the comand prompt window! (Do this atleast once before closing the game)
8. Close node window

========================================



Segmentation:
=======================================
If all has gone well you should have an .avi file with game play and a data.txt file game data.

1. rename the .avi file to input.avi

2. Run RecordingSlicer.py
Follow the instructions: Enter the time at the bottom of the terminal in the extracted start image.
		         Enter you in game name (same as in the data.txt file).
			 You should be presented with a list of times in miliseconds.

5. Press enter and your clips should appera in the output folder.

========================================

I would recomend checking each one as sometimes (such as when the bomb kill the person you are spectating) it incorrectly captuers.
I would also recomend moving the files out of the output fold once you've checked them.





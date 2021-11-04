# GSGO Clip Generator
A system to cut extract kills form gameplay recordings using Global Offensive Game State Integration.

The system is baced around synchronising the recording from OBS with the data from the Game State Integration. It is designed to generate 1 second long clips with the kill half way through.
If OBS is setup as correctly the clips should be lossless and 60fps.


## Requirements:
* Python (https://www.python.org/downloads/)
* NodeJs (https://nodejs.org/en/download/)
* OBS    (https://obsproject.com/download)


# Setup:

1. OBS Settings (settings button bottem right)
	1. Set recording
		>_<Settings>Output>Recording Quality> _**Lossless Qualitym Tremendously Large File Size**
	3. Recording Path
		>_Settings>Output>Recording Path> **[Same location as RecordingSlicerVxxx.py]**_
	4. Record Hotkey
		>_Settings>Hotkeys>Start Recording: **[Start Recording KEY]**_ i.e. F8
	5. Record Hotkey
		>_Settings>Hotkeys>Start Stop Recording: **[Stop Recording KEY]**_ i.e. F9
	
	6. FPS
		>_Settings>Video>FPS Values:_ **60**

2. Global Offensive Game State Integration
	* Copy file:  
		**`gamestate_integration_yourservicenamehere.cfg`**  
		into  
		`\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg`

	i.e. steam libary location, mine is (`E:\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg`)


# Recording:

1. Run the CSGOStats.js applicaton using node.  
	- Option A. Start a command promt and navigate to the file (in it's current location), then run `node CSGOStats.js`  
	  
	- Optoin B. Right click the `CSGOStats.js` and _Open With > Choose another app> more apps >_ `"C:\Program Files\nodejs\node.exe"` **_(recommended)_**  
        _(Option B will allow you to run the node application in future by doubble clicking it.)_

2. Launch OBS, *(don't start recording yet)*
3. Join a CSGO session.
4. Tab to the node comand prompt window.
5. Once a stream of numbers starts, Press record using your hot key (i.e. f8) ***ENSURING THE TERMINAL IS IN THE RECORDING AREA!***
6. Play a round (first to 8). _(I recommend only playing one round as the recording is huge and will be 45gb+)_ but the system does now supports endless rounds.
7. Access the menu to trigger a save of the game data. _(Alt+F4 will **NOT** trigger save)_ (Do this atleast once before closing the game)
8. Close node window


# Convert to Clips:

If all has gone well you should have an .avi file with game play and a data.txt file of game data.

1. Rename the .avi file to `input.avi`

2. Run `RecordingSlicer.py`  
Follow the instructions:  
	- Enter the time at the bottom of the terminal in the extracted start image.  
	- Enter you in game name (same as in the data.txt file).  
	- You should be presented with a list of times in miliseconds.  

3. Press <kbd>ENTER</kbd> and your clips should appear in the `\output` folder.


**! I recommend checking each one as sometimes (such as when the bomb kill the person you are spectating) it incorrectly captuers.**  
**! I also recomend moving the files out of the output folder once you've checked them.**

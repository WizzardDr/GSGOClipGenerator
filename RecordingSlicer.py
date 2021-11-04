import subprocess
import os

#videoFilename = str(input("Enter Gameplay Video file name (ensure it share the same directory as split.py): "))
#dataFilename = str(input("Enter Gameplay Data file name (ensure it share the same directory as split.py): "))
videoFilename = "input.avi"
dataFilename = "data.txt"


subprocess.call(["ffmpeg.exe", "-hide_banner", "-loglevel", "error", "-i", videoFilename, "-vf", "select=eq(n\\,1)", "-vframes", "1", "firstFrame.jpeg"])
subprocess.run(["explorer", "firstFrame.jpeg"])

kills = []

#print(subprocess.run(["stat",videoFilename]))
#wmic datafile where name=C:\\Users\\Matt\\Desktop\\DemoGameplay\\Clip Generator\\input.avi get creationdate | findstr /brc:[0-9]
fileTime = round(float(os.path.getctime(videoFilename)),3)*1000
print(str(fileTime)[7:-3])
fileTimeStartDigits = str(fileTime)[4:-7]
timeOffset = int(fileTimeStartDigits + str(input("Enter time offset (time at the bottem of the terminal): ")))


name = str(input("Enter In-Game Name: "))
#name = ""

os.remove("firstFrame.jpeg")

f = open(dataFilename, "r", encoding="utf8")
data = f.read()
lines = data.split("\n")
k=0

for lineNum in range(0,len(lines)):
    a = lines[lineNum].split(",")
    if(a[1] == name):
        if(k < int(a[2])):
            k = int(a[2])
            a[0] = int(a[0]) - timeOffset
            kills += [a[0]]
            print(a)
    else:
        k = 0
input(">")
for killTime in kills:
    outputFilename = "output\\" + str(killTime + timeOffset) + "." + videoFilename.split(".")[1]
    startTime = str((killTime/100)-0.5)
    subprocess.run(["ffmpeg.exe", "-hide_banner", "-loglevel", "error", "-ss", startTime, "-i", videoFilename, "-c", "copy", "-t", "1", outputFilename])
input(">")

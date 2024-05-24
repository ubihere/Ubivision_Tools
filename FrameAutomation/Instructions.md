# Frame Automation
Takes mp4 files and converts the frames to images

## Instructions
- Put all videos you want to extract frames from in the same directory as main.py
- Change the "SAVING_FRAMES_PER_SECOND" variable at the top of main.py to change the number of frames that will be saved per second
- Run the program and the frames will be stored in the "frames" folder

## Extra Notes
- Videos must be a mp4
- If you get a "divide by 0" error, then the mp4 that it outputted the error with is messed up. Make sure the mp4 video can be played before you put it into the directory
- When running the program, the old "frames" folder will be overridden, so save all images from the folder if you want to run the program again but keep the old frames
- There is extra commented out code at the bottom for a future implementation that compares images and deletes similar ones
## Installations
- Install datetime
- Install cv2
- Install numpy
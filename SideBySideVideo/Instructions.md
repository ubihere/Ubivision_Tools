# Ubivision_Tools
Takes multiple vidoes and overlays them together into one video
## Instructions
- Put the videos you want to overlay in the same directory as videoOverlay.py
- Make however many clip variables in videoOverlay.py as there are videos using the format already used by using VideoFileClip("nameOfVideo")
- Change the final_clip array to use however many videos you want (the shape of the array determines how the videos are put together, i.e. a 2x3 array will have three videos on top and three videos on bottom)
- The final video will be in the directory as "output.mp4"
## Installations
- Install moviepy
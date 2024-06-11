import imageio.v2 as imageio
import os

image_folder = 'images'
images = []
currentDirectory = os.getcwd()

for filename in os.listdir(currentDirectory):
    if filename == image_folder:
        imageDirectory = os.path.join(currentDirectory, filename)
        for image in sorted(os.listdir(imageDirectory)):
            images.append(imageio.imread(os.path.join(imageDirectory, image)))

currentDirectory = os.getcwd()
gifName = os.path.join(currentDirectory, "generatedGif.gif")
imageio.mimsave(gifName, images)

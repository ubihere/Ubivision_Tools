"""
This program takes all mp4 files and converts the frames to images and stores them in a file.
The number of frames saved per second can be changed in the variable "SAVING_FRAMES_PER_SECOND".
The mp4 files need to be in the source directory folder where main.py is located.
Make sure the mp4 files are able to be opened and watched before you put them in or you will get a divide by 0 error
The images are saved in the "frames" folder.
"""

from datetime import timedelta
import cv2
import numpy as np
import os
# from PIL import Image
# import imagehash

# i.e if video of duration 30 seconds, 10 would save 10 frames per second = 300 frames saved in total
SAVING_FRAMES_PER_SECOND = 1

fileNumber = 1

# cutoff = 5  # maximum bits that could be different between the hashes.


def format_timedelta(td):
    """Utility function to format timedelta objects in a cool way (e.g 00:00:20.05)
    omitting microseconds and retaining milliseconds"""
    result = str(td)
    try:
        result, ms = result.split(".")
    except ValueError:
        return (result + ".00").replace(":", "-")
    ms = int(ms)
    ms = round(ms / 1e4)
    return f"{result}.{ms:02}".replace(":", "-")


def get_saving_frames_durations(cap, saving_fps):
    """A function that returns the list of durations where to save the frames"""
    s = []
    # get the clip duration by dividing number of frames by the number of frames per second
    fps = cv2.CAP_PROP_FPS
    clip_duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps
    # use np.arange() to make floating-point steps
    for i in np.arange(0, clip_duration, 1 / saving_fps):
        s.append(i)
    return s


def main(video_file, fileNum):
    filename, _ = os.path.splitext(video_file)

    # filename += "-opencv"
    # make a folder by the name of the video file
    if not os.path.isdir("frames"):
        os.mkdir("frames")
    frames = "frames"
    # read the video file
    cap = cv2.VideoCapture(video_file)
    # get the FPS of the video
    fps = cap.get(cv2.CAP_PROP_FPS)
    # if the SAVING_FRAMES_PER_SECOND is above video FPS, then set it to FPS (as maximum)
    saving_frames_per_second = min(fps, SAVING_FRAMES_PER_SECOND)
    # get the list of duration spots to save
    saving_frames_durations = get_saving_frames_durations(cap, saving_frames_per_second)
    # start the loop
    count = 0
    while True:
        is_read, frame = cap.read()
        is_read2, frame2 = cap.read()
        if not (is_read | is_read2):
            # break out of the loop if there are no frames to read
            break
        # get the duration by dividing the frame count by the FPS
        frame_duration = count / fps
        try:
            # get the earliest duration to save
            closest_duration = saving_frames_durations[0]
        except IndexError:
            # the list is empty, all duration frames were saved
            break
        if frame_duration >= closest_duration:
            # if closest duration is less than or equals the frame duration,
            # then save the frame
            frame_duration_formatted = format_timedelta(timedelta(seconds=frame_duration))

            cv2.imwrite(os.path.join(frames, f"Video " + str(fileNum) + f" frame{frame_duration_formatted}.jpg"), frame)
            # drop the duration spot from the list, since this duration spot is already saved
            try:
                saving_frames_durations.pop(0)
            except IndexError:
                pass
        # increment the frame count
        count += 1



if __name__ == "__main__":
    import sys

    directory = os.fsencode(os.getcwd())

    for file in os.listdir(directory):
        fileName = os.fsdecode(file)
        if fileName.endswith(".mp4"):
            # print(os.path.join(directory, filename))
            print(fileName)
            main(fileName, fileNumber)
            fileNumber += 1

"""
(Future code for deleting similar images)
"""
'''
    # Define the folder name within the current directory
    folder_name = "frames"

    # Get the path to the folder
    folder_path = os.path.join(os.getcwd(), folder_name)

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        # List all files in the folder
        files = os.listdir(folder_path)

        # Loop through the files
        fileArray = ["one", "two"]
        for file in files:
            fileArray[0] = file
            hash0 = imagehash.average_hash(Image.open(file))
            hash1 = imagehash.average_hash(Image.open(file2))
            if hash0 - hash1 < 1000000000:
                file += "DELETE"

    else:
        print(f"The folder '{folder_name}' does not exist in the current directory.")

'''
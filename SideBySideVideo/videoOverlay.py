from moviepy.editor import VideoFileClip, clips_array
# Make however many clips you want and have each one the same name that's in the directory
clip1 = VideoFileClip("del-2_whiteboard_merged.mp4")
clip2 = VideoFileClip("del-3_whiteboard_merged.mp4")
clip3 = VideoFileClip("del-4_whiteboard-merge.mp4")
clip4 = VideoFileClip("del-5_whiteboard_merged.mp4")
clip5 = VideoFileClip("del-6_whiteboard_merged.mp4")
clip6 = VideoFileClip("del-7_whiteboard_merged.mp4")
clip7 = VideoFileClip("del-8_whiteboard_merged.mp4")
# Create an array with the clips (the array structure will be the same way the videos are laid out)
# i.e. if you have a 2x3 array, the output will be a 2x3 array of videos (3 videos on top and 3 videos on bottom)
final_clip = clips_array([[clip1, clip2, clip3, clip4, clip5, clip6, clip7]])
# Write it to an output file
final_clip.write_videofile("output.mp4")

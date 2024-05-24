import os
from tkinter import filedialog

class Class:
    def __init__(self):
        self.filepath = ""
        self.video_paths = []
        self.running = True


    def file_select(self):
        self.filepath = filedialog.askdirectory()
        if not self.filepath:
            print("No folder selected. Program exiting.")
            self.running = False
            return

        self.video_paths.clear()

        video_files = sorted([filename for filename in os.listdir(self.filepath)
                              if filename.endswith(('.mp4', '.avi', '.mkv', '.mov'))])

        with open('files.txt', 'w+') as files:
            for filename in video_files:
                video_path = os.path.join(self.filepath, filename)
                self.video_paths.append(video_path)
                files.write(video_path + '\n')


    def process_videos(self):

        if not self.video_paths:
            print("No videos found.")
            return

        with open('files.txt', 'w') as text_file:
            for video_path in self.video_paths:
                text_file.write(f"file '{video_path}'\n")

        output_path = os.path.join(os.getcwd(), 'merged_videos')

        output_video = os.path.join(output_path, f'{self.merged_name}.mp4')
        ffmpeg_command = f"ffmpeg -f concat -safe 0 -i {'files.txt'} -c copy {output_video}"
        os.system(ffmpeg_command)

        os.remove('files.txt')
        print("Videos concatenated.")

    def start(self):

        while self.running:
            choice = input("Enter 'select' to choose a directory or 'merge' to merge videos, or 'exit' to quit: ")
            if choice == "select":
                self.file_select()
            elif choice == "merge":
                self.merged_name = input("Enter a name for the merged video: ")
                self.process_videos()
            elif choice == "exit":
                self.running = False
            else:
                print("Invalid choice.")

run = Class()
run.start()
# Make sure both files are in the same directory as this script
# Replace first two .mp4 files into the two that you want to stitch together
ffmpeg \
  -i oldModel.mp4 \
  -i newModel.mp4 \
  -i thirdVid.mp4 \
  -filter_complex '[0:v]pad=iw*3:ih[int];[int][1:v]overlay=W/3:0[vid];[int][1:v]overlay=2*W/3:0[vid2]' \
  -map '[vid]' '[vid2]' \
  -c:v libx264 \
  -crf 23 \
  -preset veryfast \
  output.mp4
import subprocess

def download_segmented_video(video_url, start, end, output_file): # main function
  ffmpeg_command = (
      "ffmpeg",
      "-ss", start,       # start at given time
      "-i", video_url,    # input url
      "-t", end,          # duration
      "-c", "copy",       # copy codec
      output_file         # output file
  )
  subprocess.run(ffmpeg_command)

# Example usage:
video_url = "https://example.com/video.mp4"
start = "00:00:10"  # start at 10 seconds and time format should be hh:mm:ss edit example timecode before run
end = "00:00:20"    # end at 20 seconds and time formate should be hh:mm:ss edit example timecode before run
output_file = "segmented_video.mp4"
download_segmented_video(video_url, start, end, output_file)

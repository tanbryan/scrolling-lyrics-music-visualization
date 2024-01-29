# import subprocess
# import os

# def video_with_scrolling_subtitles(input_video, lyrics_text_file, output_video):
#     """
#     Use FFmpeg to merge an MP4 video with an MP3 audio and scrolling lyrics.

#     Parameters:
#         input_video (str): Path to the input video file.
#         lyrics_text_file (str): Path to the lyrics text file.
#         output_video (str, optional): Path to the output video file. Default is "output_video.mp4".

#     Returns:
#         None
#     """

#     """ Configuration Variables """
#     fontfile_path = "test/NotoSansSC-VariableFont_wght.ttf"  # font style 
#     fontsize = "40"  # font size
#     fontcolor = "white"  # font color 
#     resolution_phone = "1080x1920"  # video reolution (phone)
#     resolution_comp = "1920x1080"  # video reolution (computer)


#     """ Dimensions for the lyrics subtitles """
#     box_width = 1080  
#     box_height = 1500  
#     box_x = 0  
#     box_y = (1920 - box_height) / 2  
    
#     ffmeg_filter = (
#         f"[0:v]scale={resolution_phone}[scaled];"
#         f"[scaled]drawbox=w={box_width}:h={box_height}:x={box_x}:y={box_y}:c=white:t=fill[box_video];"
#         f"[0:v]scale={resolution_phone}[scaled_2];"
#         f"[scaled_2]crop={box_width}:{box_height}:{box_x}:{box_y}[cropped];"
#         f"[cropped]drawtext=textfile={lyrics_text_file}:fontfile={fontfile_path}:fontsize={fontsize}:fontcolor={fontcolor}:x=(w-text_w)/2:y=(h-text_h)/2-(t*50)[texted];"
#         f"[box_video][texted]overlay={box_x}:{box_y}[v];"
#     )



#     # FFmpeg command 
#     ffmpeg_command = [
#         # "ffmpeg", "-y",  # to overwrite
#         "ffmpeg",
#         "-i", input_video,
#         "-filter_complex",
#         ffmeg_filter,
#         "-map", "[v]",
#         "-c:v", "libx264",
#         output_video
#     ]
    
#     print(ffmpeg_command)

#     # try:
#     #     subprocess.run(ffmpeg_command, check=True, stderr=subprocess.STDOUT)
#     #     print(f"Video with subtitles created: {output_video}")
#     # except subprocess.CalledProcessError as e:
#     #     print(f"Error occurred while creating video with subtitles. Details: {e}")

# if __name__ == "__main__":
#     video_file = "/Users/bryannnh/Desktop/mp4-generator/test/2.mp4"
#     lyrics_text_file = "/Users/bryannnh/Desktop/mp4-generator/test/2.txt"
#     output_video_path = "output_no_sound.mp4"

#     video_with_scrolling_subtitles(video_file, lyrics_text_file, output_video_path)
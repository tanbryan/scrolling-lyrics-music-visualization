import subprocess
import os

def video_with_floating_subtitles(input_video, lyrics_text_file, output_video):
    """
    Use FFmpeg to merge an MP4 video with an MP3 audio and scrolling lyrics.

    Parameters:
        input_video (str): Path to the input video file.输入视频文件的路径。
        lyrics_text_file (str): Path to the lyrics text file.歌词文本文件的路径。
        output_video (str, optional): Path to the output video file. Default is "output_video.mp4". 输出视频文件的路径。默认为"output_video.mp4"。

    Returns:
        None
    """

    """ Configuration Variables """
    Font_name = "Arial"  # font style 
    font_size = "40"  # font size
    font_color = "white"  # font color 
    resolution_phone = "1080x1920"  # video reolution (phone)
    resolution_comp = "1920x1080"  # video reolution (computer)


    ffmeg_filter = (
        f"[0:v]subtitles={lyrics_text_file}:force_style='FontName={Font_name},FontSize={font_size},PrimaryColour={font_color}'[v];"
    )
    # FFmpeg 工具， 合并字幕，mv模式，横向
    ffmpeg_command = [
        # "ffmpeg", "-y",  # to overwrite
        "ffmpeg",
        "-i", input_video,
        "-filter_complex",
        ffmeg_filter,
        "-map", "[v]",
        "-c:v", "libx264",
        output_video
    ]
    # run ffmpeg工具
    try:
        subprocess.run(ffmpeg_command, check=True, stderr=subprocess.STDOUT)
        print(f"Video with subtitles created: {output_video}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while creating video with subtitles. Details: {e}")


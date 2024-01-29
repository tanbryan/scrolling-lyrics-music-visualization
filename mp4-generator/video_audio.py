import subprocess
import os


def video_with_audio(input_video, input_audio, output_video):
    #合并音频和之前生成过的视频
    """
    Use FFmpeg to merge an MP4 video with an MP3 audio and floating subtitles.

    :param input_video: Path to the input video file.
    :param input_audio: Path to the input audio file.
    :param output_video: Path to the output video file. 
    :return: None
    """
    # ffmpeg 命令
    ffmpeg_command = [
        "ffmpeg", "-y",  # to overwrite
        # "ffmpeg",
        "-i", input_video,
        "-i", input_audio,
        "-filter_complex", 
        "[0:v]scale=1080x1920:flags=lanczos,setsar=1[v];[1:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo[a]",
        "-map", "[v]",
        "-map", "[a]",
        "-c:v", "libx264",  
        "-c:a", "aac",     
        output_video
    ]

    try:
        subprocess.run(ffmpeg_command, check=True)
        print(f"Video created: {output_video}")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while creating video with subtitles. Details: {e}")

# if __name__ == "__main__":
#     video_file = "/Users/bryannnh/Desktop/mp4-generator/output_no_sound.mp4"
#     audio_file = "/Users/bryannnh/Desktop/mp4-generator/test/3.mp3"
    
#     audio_filename_without_extension = os.path.basename(audio_file).rsplit('.', 1)[0]
#     new_folder_path = os.path.join(os.path.dirname(audio_file), audio_filename_without_extension)
#     if not os.path.exists(new_folder_path):
#         os.makedirs(new_folder_path)
    
#     output_video_path = os.path.join(new_folder_path, f"{audio_filename_without_extension}"+"_final.mp4")

#     video_with_audio(video_file, audio_file, output_video_path)

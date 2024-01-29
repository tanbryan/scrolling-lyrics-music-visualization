import os
import subtitle_video  
import mv_video

## 检查文件是否有效
def is_valid_file(file_path, extensions):
    return os.path.isfile(file_path) and any(file_path.endswith(ext) for ext in extensions)
## 获取用户输入的文件路径
def get_file_input(prompt, valid_extensions):
    while True:
        file_path = input(prompt).strip('\"')
        if is_valid_file(file_path, valid_extensions):
            return file_path
        else:
            print(f"Invalid file. Please ensure the file exists and is one of the following types: {valid_extensions}")

def user_prompt():
    print("""
        Welcome to the Subtitle Video Processor!
        Please provide the required file paths and select your subtitle formatting choice.
    """)

    # Get video file input
    # 获取视频文件输入
    video_file = get_file_input("Path to video file (mp4): ", [".mp4"])

    # Get audio file input
    # 音频
    audio_file = get_file_input("Path to audio file (mp3): ", [".mp3"])

    # Get subtitles file input
    # 字幕
    subtitles_file = get_file_input("Path to subtitles file (srt, lrc): ", [".srt", ".lrc"])

    ## 用户选择生成视频的格式，横向或者纵向手机滚动模式
    while True:
        user_choice = input("Choose subtitle format - Floating (1) or Scrolling (2): ")
        if user_choice in ['1', '2']:
            break
        else:
            print("Invalid choice. Please enter 1 for Floating or 2 for Scrolling.")
    #横向字幕
    if user_choice == '1':
        mv_video.video_with_floating_subtitles(video_file, subtitles_file, "output_video.mp4")
    #滚动字幕
    elif user_choice == '2':
        subtitle_video.video_with_scrolling_subtitles(video_file, subtitles_file, "output_video.mp4")

    #最后拼接音频和生成的字幕视频
    output_video_file = "output_video.mp4"
    video_with_audio(video_file, audio_file, output_video_file)
    print("Processing complete. Check the output file.")

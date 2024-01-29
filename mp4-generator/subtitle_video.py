import subprocess
import os
import ffmpeg
import pylrc

def load_lrc(lyrics_text_file):
    #读取并解析LRC格式的歌词文件。
    with open(lyrics_text_file, 'r') as f:
        lrc_content = f.read()
    return pylrc.parse(lrc_content)

def video_with_scrolling_subtitles(input_video, lyrics_text_file, output_video):
    # 使用FFmpeg将滚动字幕添加到视频中。
    """
    Use FFmpeg to merge an MP4 video with an MP3 audio and scrolling lyrics.

    Parameters:
        input_video (str): Path to the input video file.
        lyrics_text_file (str): Path to the lyrics text file.
        output_video (str, optional): Path to the output video file. Default is "output_video.mp4".

    Returns:
        None
    """

    """ Configuration Variables """
    fontfile_path = "test/NotoSansSC-VariableFont_wght.ttf"  # font style 
    fontsize = "40"  # font size
    fontcolor = "white"  # font color 
    resolution_phone = "1080x1920"  # video reolution (phone)
    resolution_comp = "1920x1080"  # video reolution (computer)
    line_spacing = 10 

    # 歌词字幕的尺寸和位置设置
    """ Dimensions for the lyrics subtitles """
    box_width = 1080  
    box_height = 1500  
    box_x = 0  
    box_y = (1920 - box_height) / 2  

    subs = load_lrc(lyrics_text_file)

    sub_filters = []
    initial_y_position = 1920/2
    # initial_y_position = (1920 - (len(subs) * (int(fontsize) + line_spacing))) //2
    input_pad = "[scaled]"
    for i, sub in enumerate(subs):
        start_time = sub.time
        end_time = subs[i+1].time if i < len(subs) - 1 else start_time + 5
        y_position = initial_y_position + i * (int(fontsize) + line_spacing)
        text = sub.text.replace("'", r"\'")
        # if sub.time == 0:
        #     y_expr = f"{y_position}"
        # else:
        y_expr = f"{y_position} - ({line_spacing} * (t - {start_time}))"
        # 创建白色字幕滤镜
        drawtext_white = (
            f"{input_pad}drawtext=text='{text}':fontfile={fontfile_path}:fontsize={fontsize}:"
            f"fontcolor=white:x=(w-text_w)/2:y={y_expr}[whiteText{i}]"
        )
        sub_filters.append(drawtext_white)
        input_pad = f"[whiteText{i}]"
    # Red text
    
            # print(y_expr)
            # 创建红色字幕滤镜
        drawtext_red = (
            f"{input_pad}drawtext=text='{text}':fontfile={fontfile_path}:fontsize={fontsize}:"
            f"fontcolor=red:enable='between(t,{start_time},{end_time})':x=(w-text_w)/2:y={y_expr}[redText{i}]"
        )
        sub_filters.append(drawtext_red)
        input_pad = f"[redText{i}]"
    # At the end of the filter chain, we'll use the last [redText] pad as the output
        # 设置滤镜链并处理视频
    scale_filter = f"[0:v]scale={resolution_phone}[scaled];"
    ffmeg_filter =scale_filter+ ';'.join(sub_filters).replace(f"[redText{len(subs)-1}]", "[v]")
    print(ffmeg_filter)


    # FFmpeg command 
        # FFmpeg命令行
    ffmpeg_command = [
        "ffmpeg", "-y",  # overwrite output if exists
        # "ffmpeg"
        "-i", input_video,
        "-filter_complex", ffmeg_filter,
        "-map", "[v]",
        "-c:v", "libx264",
        output_video
    ]

    try:
        subprocess.run(ffmpeg_command, check=True, stderr=subprocess.STDOUT)
        print(f"Video with subtitles created: {output_video}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while creating video with subtitles. Details: {e}")


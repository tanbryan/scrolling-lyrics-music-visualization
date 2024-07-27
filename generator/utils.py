import os
import subprocess
import pylrc
import cv2

def get_output_path(input_file, output_filename):
    input_dir = os.path.dirname(input_file)
    return os.path.join(input_dir, output_filename)

def is_file_valid(file_path):
    try:
        if not file_path.endswith('.mp4'):
            print(f"Error: The specified file does not have the .mp4 extension: {file_path}")
            return False

        if not os.path.isfile(file_path) or os.path.getsize(file_path) <= 0:
            print(f"Error: The specified file does not exist or is empty: {file_path}")
            return False
        cap = cv2.VideoCapture(file_path)
        if not cap.isOpened():
            print(f"Error: The specified video file could not be opened: {file_path}")
            return False
        cap.release()
        return True
    except Exception as e:
        print(f"Error: An error occurred while trying to open the video file: {file_path}")
        print(f"Exception: {e}")
        return False

def load_lrc(lyrics_text_file):
    with open(lyrics_text_file, 'r', encoding='utf-8') as f:
        lrc_content = f.read()    
    print("finished loading lrc file")
    return pylrc.parse(lrc_content)

def get_audio_duration(input_audio):
    try:
        result = subprocess.run(
            ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', input_audio],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
        duration = float(result.stdout)
        return duration
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while getting audio duration: {e}")
        return None
    except ValueError as e:
        print(f"Could not convert duration to float: {e}")
        return None

def format_timestamp(seconds):
    if seconds is None:
        return "00 00"
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02} {seconds:02}"

def hex_to_rgb_normalized(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))

def validate_file_path(file_path, file_type):
    # Ensure the file path has the correct extension
    print(file_type)
    if file_type == 'lyrics':
        required_extension = '.lrc'
    elif file_type == 'audio':
        required_extension = '.mp3'
    else:
        print(f"Error: Unsupported file type: {file_type}")
        return False
    
    if not file_path.endswith(required_extension):
        print(f"Error: The specified {file_type} file must have the extension {required_extension}")
        return False

    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"Error: The specified {file_type} file does not exist: {file_path}")
        return False

    try:
        if file_type == 'audio':
            with open(file_path, 'rb') as f:
                f.read(1)  
        elif file_type == 'lyrics':
            with open(file_path, 'r', encoding='utf-8') as f:
                f.read(1)
        else:
            print(f"Error: Unsupported file type: {file_type}")
            return False
        return True
    except Exception as e:
        print(f"Error: The specified {file_type} file could not be opened: {file_path}")
        print(f"Exception: {e}")
        return False

def print_welcome_message():
    print("\033[1;34m" + "*                                                                  *" + "\033[0m")
    print("\033[1;32m" + "*              🎵 Welcome to the AI MV Generator!                  *" + "\033[0m")
    print("\033[1;34m" + "*                                                                  *" + "\033[0m")
    print("\033[1;36m" + "*  Transform your audio and lyrics into a stunning music video     *" + "\033[0m")
    print("\033[1;34m" + "*                                                                  *" + "\033[0m")
    print("\033[1;35m" + "*            🎬 Let's get started on your masterpiece.             *" + "\033[0m")
    print("\033[1;34m" + "*              Please follow the prompts below.                    *" + "\033[0m")
    print("\033[1;33m" + "* 📁 All outputs will be saved in your mp3 and lrc files directory *" + "\033[0m")

def print_audio_input_prompts():
    print("\n❗️Please enter the path for the audio file (e.g., LoveStory-TaylorSwift.mp3):")
    print("❗️Make sure the mp3 file is named in the sample format")
    print("\033[1;31m❗️songname-singername.mp3 without space between, paste your mp3 file path here:\033[0m")
    input_audio = input().strip()
    while not validate_file_path(input_audio, "audio"):
        print("❗️Please enter a valid audio file path:")
        input_audio = input().strip()
    
    return input_audio

def print_lyrics_input_prompts():
    print("\n❗️Please enter the path for the lyrics file (e.g., LoveStory-TaylorSwift.lrc):")
    print("❗️Make sure the lrc file is named in the sample format")
    print("❗️songname-singername.lrc without space between")
    print("\033[1;31m❗️Make sure there is no \"'\"(single quotation marks)symbol in your lyrics file, it will confuse ffmpeg\033[0m")
    print("\033[1;31m❗️paste your lrc file path here:\033[0m")
    input_lyrics = input().strip()
    while not validate_file_path(input_lyrics, "lyrics"):
        print("❗️Please enter a valid lyrics file path:")
        input_lyrics = input().strip()
        
    return input_lyrics

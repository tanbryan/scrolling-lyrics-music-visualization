import os
import subprocess
import pylrc

def get_output_path(input_file, output_filename):
    input_dir = os.path.dirname(input_file)
    return os.path.join(input_dir, output_filename)

def is_file_valid(filepath):
    return os.path.isfile(filepath) and os.path.getsize(filepath) > 0

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
    if not os.path.isfile(file_path):
        print(f"Error: The specified {file_type} file does not exist: {file_path}")
        return False
    try:
        with open(file_path, 'rb') as f:
            f.read(1)  # Try reading the first byte to ensure the file can be opened
        return True
    except IOError as e:
        print(f"Error: The specified {file_type} file could not be opened: {file_path}")
        print(f"IOError: {e}")
        return False

def print_welcome_message():
    print("*******************************************")
    print("*                                         *")
    print("*🎵 Welcome to the Ultimate MV Generator! *")
    print("*                                         *")
    print("*******************************************\n")
    print("* Transform your audio and lyrics into a  *")
    print("* stunning music video with ease!         *")
    print("*                                         *")
    print("* Let's get started on your masterpiece.  *")
    print("* Please follow the prompts below.        *")
    print("* All outputs will be saved in your mp3 and lrc files directory *")
    print("*******************************************\n")

def print_audio_input_prompts():
    print("\n❗️Please enter the path for the audio file (e.g., LoveStory-TaylorSwift.mp3):")
    print("❗️Make sure the mp3 file is named in the sample format")
    print("❗️songname-singername.mp3 without space between, paste your mp3 file path here:")
    input_audio = input().strip()
    while not validate_file_path(input_audio, "audio"):
        print("❗️Please enter a valid audio file path:")
        input_audio = input().strip()
    
    return input_audio

def print_lyrics_input_prompts():
    print("\n❗️Please enter the path for the lyrics file (e.g., LoveStory-TaylorSwift.lrc):")
    print("❗️Make sure the lrc file is named in the sample format")
    print("❗️songname-singername.lrc without space between")
    print("❗️Make sure there is no \"'\" symbol in your lyrics file, it will confuse ffmpeg")
    print("❗️paste your lrc file path here:")
    input_lyrics = input().strip()
    while not validate_file_path(input_lyrics, "lyrics"):
        print("❗️Please enter a valid lyrics file path:")
        input_lyrics = input().strip()
        
    return input_lyrics

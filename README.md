# AI MV Generator
The AI MV Generator is a Python-based tool that allows users to transform audio and lyrics into stunning music videos with scrolling subtitles and visual effects. This tool is optimized for phone resolution and has been fine-tuned through extensive debugging to ensure high-quality output.

🌹🌹🌹🌹🌹🌹 AI background still under testing and finetuning

## Introduction

The AI MV Generator uses various Python libraries to process audio files, create visual effects, and overlay subtitles. A crucial component of this tool is `ffmpeg`, a powerful multimedia framework used to handle audio and video processing. The generated music videos are designed to be visually appealing and synchronized with the audio and lyrics. (BTW, ffmpeg syntax is very hard to follow and debug 😭)

## Sample Output

The AI MV Generator produces several output files during its process, each showcasing different stages of the video generation. Below are descriptions and links to sample outputs:

### Visual Output

This video demonstrates the visual effects generated based on the audio file. The visual elements are synchronized with the audio, providing an engaging visual representation of the music.

![Visual Output]

### Cropped Subtitle

This video shows the scrolling subtitles (similar to any music player app) added to the video. The subtitles are synchronized with the lyrics and scroll smoothly, making it easy to follow along with the music.

![Scrolling Subtitle]

### Final Output

The final video combines all features: visual effects, scrolling subtitles, and additional metadata like the title, author, and timestamp. This video is fully synchronized and optimized for phone resolution, providing a high-quality music video experience.

![Final Output]

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.8 or higher
- `ffmpeg` installed and available in your system's PATH
- Required Python packages installed

### Installing `ffmpeg`

#### Windows:

1. Download `ffmpeg` from the [official website](https://ffmpeg.org/download.html).
2. Extract the downloaded archive to a folder of your choice.
3. Add the `bin` folder to your system's PATH:
    - Open the Start Search, type in "env", and select "Edit the system environment variables".
    - In the System Properties window, click on the "Environment Variables" button.
    - In the Environment Variables window, find the `Path` variable in the "System variables" section and select it. Click on "Edit".
    - Click "New" and add the path to the `bin` folder of the extracted `ffmpeg` archive. Click "OK" to apply the changes.

#### macOS:

1. Install `Homebrew` if you don't have it installed. Open the Terminal and run:

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. Use `Homebrew` to install `ffmpeg`:

    ```bash
    brew install ffmpeg
    ```

#### Linux:

1. For Debian-based distributions (e.g., Ubuntu), open the Terminal and run:

    ```bash
    sudo apt update
    sudo apt install ffmpeg
    ```

2. For Red Hat-based distributions (e.g., Fedora), open the Terminal and run:

    ```bash
    sudo dnf install ffmpeg
    ```

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/tanbryan/AI-mv-generator
    cd AI-mv-generator
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Sample Usage

1. **Prepare your input files:**
    - Audio file (e.g., `LoveStory-TaylorSwift.mp3`)
    - Lyrics file (e.g., `LoveStory-TaylorSwift.lrc`)

2. **Run the script:**

    ```bash
    python -m ai_mv_generator
    ```

3. **Follow the prompts to enter the paths for the audio and lyrics files:**

    ```
    Please enter the path for the audio file (e.g., LoveStory-TaylorSwift.mp3):
    <path_to_your_audio_file>
    Please enter the path for the lyrics file (e.g., LoveStory-TaylorSwift.lrc):
    <path_to_your_lyrics_file>
    ```

## Features

- **Visual Effects:** Generates a visual representation of the audio file with customizable colors and styles.
- **Scrolling Subtitles:** Adds scrolling subtitles synchronized with the audio.
- **Title and Metadata:** Adds title, author, and timestamp information to the video.
- **Optimized for Phone Resolution:** Settings are fine-tuned for optimal display on phone screens.

## Configuration Settings

The tool uses a configuration (`settings.py`) to manage various parameters:
Configuration settings for generating music videos with scrolling subtitles and visual effects.
These settings are optimized for phone resolution and have been fine-tuned through extensive debugging.

## Credits

This project was developed by me, bryannnh. It leverages the power of Python and various libraries like `librosa`, `matplotlib`, and `ffmpeg` to create high-quality music videos.

The idea for the audio analyzer and visualization using `librosa` was inspired by the post on Medium: [How to Create a Music Visualizer](https://medium.com/analytics-vidhya/how-to-create-a-music-visualizer-7fad401f5a69).

Special thanks to this YouTube video for providing sample tests: [Love Story - Taylor Swift (You Belong With Me) - Test Sample](https://www.youtube.com/watch?v=8xg3vE8Ie_E).


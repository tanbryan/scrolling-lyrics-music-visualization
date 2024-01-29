
# MP4 Generator

MP4 Generator is a Python application for processing and generating MP4 videos with customizable subtitles. It provides functionality to merge videos with subtitles and audio files, and supports both floating and scrolling subtitle formats.

## Installation

### Prerequisites

- Python 3.x
- FFmpeg

Ensure Python and FFmpeg are installed on your system. FFmpeg can be downloaded from [FFmpeg's official website](https://ffmpeg.org/download.html).

### Clone the Repository

Clone the MP4 Generator repository to your local machine:

```
git clone https://github.com/tanbryan/mp4-generator
cd mp4_generator
```

### Install Dependencies

Install the required Python libraries:

```
pip install librosa biopython praatio tqdm requests colorama pyyaml pynini
```

### Installing Montreal Forced Aligner (MFA)
"TO BE DONE, do not need this step"

1. Clone the MFA repository:

    ```
    git clone https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner
    cd Montreal-Forced-Aligner
    pip install -e .
    ```

2. Create a conda environment:

    - Linux/MacOSX: `conda create -n aligner kaldi pynini`
    - Windows: `conda create -n aligner kaldi`

3. Activate the environment:

    ```
    conda activate aligner
    ```

4. Install MFA:
    
    - From PyPi: `pip install montreal-forced-aligner`
    - From GitHub: `pip install git+https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner.git`

   Or, from inside the MFA repository root directory:

    ```
    pip install -e .
    ```

   Alternatively:

    ```
    python setup.py install
    ```

   Or:

    ```
    python setup.py develop
    ```

## Usage

To run the MP4 Generator, navigate to the project directory and execute:

```
python mp4_generator
```

Follow the on-screen prompts to provide the required file paths and select your subtitle formatting choice.

## Features

- Merge video and audio files
- Add customizable subtitles to videos
- Support for floating and scrolling subtitles
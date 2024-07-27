from .audio_visualizer import AudioVisualizer
from .scrolling_subtitles import ScrollingSubtitlesGenerator
from .settings import settings
from .utils import validate_file_path, print_welcome_message, print_audio_input_prompts, print_lyrics_input_prompts

def main(settings):
    ### sample test inputs
    # input_audio = "replace your audio file path here"
    # input_lyrics = "replace your lyrics file path here"

    print_welcome_message()
    input_audio = print_audio_input_prompts()
    input_lyrics = print_lyrics_input_prompts()

    audio_visualizer = AudioVisualizer(settings)
    scrolling_subtitles_generator = ScrollingSubtitlesGenerator(settings)

    audio_visualizer.stereo_convert(input_audio)
    audio_visualizer.visual(input_audio)
    audio_visualizer.overlay_cropped_visual_video(input_audio)

    scrolling_subtitles_generator.video_with_scrolling_subtitles(input_audio, input_lyrics)
    crop_params = scrolling_subtitles_generator.crop_video(input_audio)
    scrolling_subtitles_generator.overlay_cropped_video(input_audio, crop_params)
    scrolling_subtitles_generator.add_title(input_audio)

if __name__ == "__main__":
    main(settings)

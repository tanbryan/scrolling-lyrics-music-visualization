"""
🌹🌹🌹🌹🌹🌹
These settings are optimized for phone resolution, 
only revise when really need it, some variables take time to debug
🌹🌹🌹🌹🌹🌹
"""
settings = {
    #  font file used for text (ScrollingSubtitlesGenerator).
    'fontfile_path': "mp4_generator/ref/fonts/Noto_Sans_SC/static/NotoSansSC-Regular.ttf",

    # Font size for the subtitles (ScrollingSubtitlesGenerator).
    'font_size': 48,

    # Spacing between lines of subtitles (ScrollingSubtitlesGenerator).
    'subtitle_line_spacing': 46,

    # Color of the subtitle text (ScrollingSubtitlesGenerator).
    'font_color': "#D9D9D9@0.3",

    # Color of the highlighted subtitle text  (ScrollingSubtitlesGenerator).
    'highlight_fontcolor': "#D9D9D9@1.0",

    # Starting vertical position (in pixels) for the subtitles (ScrollingSubtitlesGenerator).
    'subtitle_starting_position': 1200,

    # Resolution of the video in width x height format (ScrollingSubtitlesGenerator, AudioVisualizer).
    'resolution': "1080x1440",

    # Font size for the title text (ScrollingSubtitlesGenerator).
    'title_size': 48,

    # Spacing between lines of the title text (ScrollingSubtitlesGenerator).
    'title_line_spacing': 12,

    # Color of the title text (ScrollingSubtitlesGenerator).
    'title_color': "white@1.0",

    # Vertical position (in pixels) for the title text (ScrollingSubtitlesGenerator).
    'title_position': 420,

    # Font size for the author text (ScrollingSubtitlesGenerator).
    'author_fontsize': 36,

    # Font size for the timestamp text (ScrollingSubtitlesGenerator).
    'timestamp_fontsize': 36,

    # Color of the author text (ScrollingSubtitlesGenerator).
    'author_color': "#ffffff@0.6",

    # Color of the timestamp text (ScrollingSubtitlesGenerator).
    'timestamp_color': "#ffffff@0.6",

    # Default background image used in the video
    'background_image_path': "mp4_generator/ref/default_backgrounds/default.png",

    # Crop area (x, y, width, height) for the video (AudioVisualizer).
    'crop_size': (80, 560, 900, 272*2),

    # Visual effect plot area (x_min, x_max, y_min, y_max) for the visual effects (AudioVisualizer).
    'plot_size': (0, 3000, -100, 100),

    # Color used for the visual element bars (AudioVisualizer).
    'fig_color': '#9BB8ED'
}

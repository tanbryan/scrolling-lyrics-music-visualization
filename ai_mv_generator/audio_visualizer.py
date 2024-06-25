import subprocess
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import librosa
from scipy.ndimage import uniform_filter1d
import matplotlib.colors as mcolors
from PIL import Image
import gc

from .audio_analyzer import AudioAnalyzer
from .utils import get_output_path, is_file_valid, hex_to_rgb_normalized

class AudioVisualizer:
    """
    Create visual effects for audio files, convert audio to stereo, generate visual representations,
    and overlay visuals onto background videos.

    Attributes:
    settings (dict): Configuration settings for visual generation and audio processing.

    Methods:
    stereo_convert(audio_input):
        Converts the input audio file to stereo.
    create_custom_colormap(hex_color):
        Creates a custom colormap for visual effects.
    visual(input):
        Generates a visual representation of the audio file.
    overlay_cropped_visual_video(audio_input):
        Overlays the generated visual video onto a background video.
    """
    def __init__(self, settings):
        self.settings = settings

    def stereo_convert(self, audio_input):
        output = get_output_path(audio_input, 'stereo.wav')
        if is_file_valid(output):
            print("\n✅stereo.wav already exists and is valid. Skipping....\n")
            return output
        command = f"ffmpeg -y -i {audio_input} -ac 2 {output}"
        print("\n🔄converting audio to stereo\n")
        subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)  
        print(f"✅audio converted to stereo as stereo.wav\n")
        return output

    def create_custom_colormap(self, hex_color):
        rgb_color = hex_to_rgb_normalized(hex_color)
        return mcolors.LinearSegmentedColormap.from_list('custom_cmap', [rgb_color, (1, 1, 1)])

    def visual(self, input):
        output = get_output_path(input, 'visual_output.mp4')

        if is_file_valid(output):
            print("✅visual_output.mp4 already exists and is valid. Skipping.....\n")
            return output

        background_image_path = self.settings['background_image_path']
        crop_rect = self.settings['crop_size']
        plot_size = self.settings['plot_size']

        analyzer = AudioAnalyzer()
        analyzer.load(input)

        data, sample_rate = librosa.load(input, sr=None)
        total_frames = len(data)
        frames_per_chunk = int(sample_rate / 10.0)
        total_chunks = total_frames // frames_per_chunk

        frequencies = np.arange(100, plot_size[1], 100)
        n_frequencies = len(frequencies)

        px = 1 / plt.rcParams['figure.dpi']
        figsize = (round(crop_rect[2] * px, 1), round(crop_rect[3] * px, 1))
        fig, ax = plt.subplots(figsize=figsize)
        fig.patch.set_facecolor('none')
        ax.set_facecolor('none')
        fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
        ax.set_axis_off()

        if background_image_path:
            image = plt.imread(background_image_path)
            x, y, w, h = crop_rect
            image_cropped = image[y:y+h, x:x+w]

        bar_width = (plot_size[1] - plot_size[2]) / n_frequencies * 0.8
        bars = ax.bar(frequencies, np.zeros(n_frequencies), width=bar_width, align='center', color=self.settings['fig_color'])

        custom_cmap = self.create_custom_colormap(self.settings['fig_color'])
        norm = mcolors.Normalize(vmin=0, vmax=1)

        def update_plot(frame):
            start = frame * frames_per_chunk
            end = start + frames_per_chunk
            if end > total_frames:
                end = total_frames

            chunk_time = librosa.samples_to_time(np.arange(start, end), sr=sample_rate)
            time_point = chunk_time[len(chunk_time) // 2]
            decibels = [analyzer.get_decibel(time_point, freq) for freq in frequencies]

            min_db = min(decibels)
            max_db = max(decibels)
            normalized_decibels = [(db - min_db) / (max_db - min_db) * 100 for db in decibels]
            filters = uniform_filter1d(normalized_decibels, size=5)

            ax.clear()
            ax.imshow(image_cropped, aspect='auto', extent=plot_size)
            ax.set_facecolor('none')
            ax.set_axis_off()
            
            shadow_bars_width = (plot_size[1] - plot_size[2]) / n_frequencies * 0.95
            shadow_bars = ax.bar(frequencies, np.zeros(n_frequencies), width=shadow_bars_width, align='center', color=self.settings['fig_color'], alpha=0.05)
            reflection_bar_width = (plot_size[1] - plot_size[2]) / n_frequencies * 0.95
            reflection_bars = ax.bar(frequencies, np.zeros(n_frequencies), width=reflection_bar_width, align='center', color=self.settings['fig_color'], alpha=0.05)
            
            for i, (bar, reflection_bar, shadow_bar, filter) in enumerate(zip(bars, reflection_bars, shadow_bars, filters)):
                bar.set_height(filter)
                shadow_bar.set_height(filter + 5)
                reflection_bar.set_height(-filter)

                if np.isnan(bar.get_height()):
                    print(f"Skipping bar at position {bar.get_x()} due to NaN height")
                    continue

                gradient = np.linspace(0, 1, int(bar.get_height() * 10)).reshape(-1, 1)
                gradient_colors = custom_cmap(norm(gradient)).reshape(-1, 4)

                x_grid, y_grid = np.meshgrid(
                    [bar.get_x(), bar.get_x() + bar.get_width()], 
                    np.linspace(0, bar.get_height(), gradient.shape[0] + 1)
                )

                shadow_bar_x_grid, shadow_bar_y_grid = np.meshgrid(
                    [shadow_bar.get_x(), shadow_bar.get_x() + shadow_bar.get_width()],
                    np.linspace(0, shadow_bar.get_height(), gradient.shape[0] + 1)
                )

                reflection_bar_x_grid, reflection_bar_y_grid = np.meshgrid(
                    [reflection_bar.get_x(), reflection_bar.get_x() + reflection_bar.get_width()],
                    np.linspace(0, reflection_bar.get_height(), gradient.shape[0] + 1)
                )

                plt.gca().pcolormesh(shadow_bar_x_grid, shadow_bar_y_grid, gradient, shading='auto', cmap=custom_cmap, alpha=0.1)
                plt.gca().pcolormesh(reflection_bar_x_grid, reflection_bar_y_grid, gradient, shading='auto', cmap=custom_cmap, alpha=0.05)
                plt.gca().pcolormesh(x_grid, y_grid, gradient, shading='auto', cmap=custom_cmap, norm=norm)

            ax.set_ylim(plot_size[2], plot_size[3])
            ax.set_xlim(plot_size[0], plot_size[1])
            percent_complete = (frame / total_chunks) * 100
            print(f"processing visual effect: {percent_complete:.2f}% complete")

            if frame % 100 == 0:
                gc.collect()

            return bars, reflection_bars

        print("🔄start creating visual effect\n")
        ani = animation.FuncAnimation(fig, update_plot, frames=total_chunks, repeat=False)
        ax.imshow(image_cropped, aspect='auto', extent=plot_size)
        ani.save(output, fps=10, codec='libx264', extra_args=['-pix_fmt', 'yuv420p'])
        plt.close(fig)
        print(f"✅visual video created at visual_output.mp4\n")
        return output

    def overlay_cropped_visual_video(self, audio_input):
        input_visual = get_output_path(audio_input, 'visual_output.mp4')
        output = get_output_path(audio_input, 'final_visual_video.mp4')

        if is_file_valid(output):
            print("✅final_visual_video.mp4 already exists and is valid. Skipping.....\n")
            return output
        print("🔄overlaying visual video to background video\n")
        background_image_path = self.settings['background_image_path']

        x, y, _, _ = self.settings['crop_size']
        overlay_command = f"[0:v]format=yuv420p[base],[1:v]format=yuv420p[cropped],[base][cropped]overlay={x}:{y}"
        ffmpeg_command = [
            "ffmpeg", "-y",
            "-i", background_image_path,
            "-i", input_visual,
            "-filter_complex", overlay_command,
            "-c:v", "libx264",
            "-crf", "18",
            "-preset", "slow",
            output
        ]
        try:
            ffmpeg_command_with_audio = ffmpeg_command + ["-map", "1:a"]
            subprocess.run(" ".join(ffmpeg_command_with_audio), shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)  
            print(f"✅overlay to background video created as final_visual_video.mp4\n")
            return output
        except subprocess.CalledProcessError:
            subprocess.run(" ".join(ffmpeg_command), shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)  

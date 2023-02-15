from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip


def merge_video_and_audio(video_filename, audio_filename=None):
    """
    Merge a video and an audio file.

    Args:
        video_filename (str): The name of the video file.
        audio_filename (str): The name of the audio file.

    Returns:
        None: The function does not return anything, it saves the merged file to disk.

    Raises:
        FileNotFoundError: If the specified video or audio file does not exist.

    """
    # Construct the file paths for the video and audio files
    video_file = f'files/{video_filename}'
    audio_file = f'files/{audio_filename}'

    video = VideoFileClip(video_file)
    audio = AudioFileClip(audio_file)

    final_video = video.set_audio(audio)

    final_video.write_videofile(f'{video_filename}', fps=video.fps, audio_codec='aac')




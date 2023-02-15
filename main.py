import logging
import pytube
import merge

OUTPUT_DIRECTORY = "files"


class DownloadVideo:
    """
    A class for downloading videos from YouTube and extracting the audio.

    Attributes:
    url (str): The URL of the video to be downloaded
    quality (str): The quality of the video to be downloaded (e.g. "720" or "1080")
    video_filename (str): The filename of the video file after it has been downloaded
    audio_filename (str): The filename of the audio file after it has been extracted
    """
    def __init__(self, url: str, quality: str):
        self.url = url
        self.quality = quality
        self.video_filename = None
        self.video_filename = self.set_video_filename()
        self.audio_filename = None
        self.audio_filename = self.set_audio_filename()

    def set_video_filename(self):
        """
        Sets the filename of the video file to be downloaded.

        Returns:
        str: The filename of the video file
        """
        yt = pytube.YouTube(self.url)
        self.video_filename = f"{yt.title}.mp4"
        return self.video_filename

    def set_audio_filename(self):
        """
        Sets the filename of the audio file to be extracted.

        Returns:
        str: The filename of the audio file
        """
        yt = pytube.YouTube(self.url)
        self.audio_filename = f"audio_{yt.title}.mp4"
        return self.audio_filename

    def download_video_and_audio(self):
        """
        Downloads the video and extracts the audio.
        """
        yt = pytube.YouTube(self.url)
        video = yt.streams.filter(res=f'{self.quality}p').first()

        logging.info(f'Starting the video download process')
        video.download(output_path=OUTPUT_DIRECTORY, filename=self.video_filename)
        logging.info(f"The video was successfully downloaded")
        # TODO: Add to check, when Quality >= 1080, then download audio too, if not, pass.
        audio = yt.streams.filter(only_audio=True).first()

        logging.info(f'Starting the audio download process')
        audio.download(output_path=OUTPUT_DIRECTORY, filename=self.audio_filename)
        logging.info(f"The audio was successfully extracted")


if __name__ == '__main__':
    download = DownloadVideo(str(input("Enter video URL: ")), (input("Enter quality (etc. 720 or 1080): ")))
    download.download_video_and_audio()
    video_file = download.video_filename
    print(video_file)
    audio_file = download.audio_filename
    print(audio_file)
    merge.merge_video_and_audio(video_file, audio_file)

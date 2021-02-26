"""
Defines the Audio class that is used to hold and play all audio files for the program.

:author: Jacob Singleton
"""

from pathlib import Path
from os import listdir
from random import randint
from playsound import playsound


class Audio:
    """
    Object that holds information about the audio files and plays them.
    """

    @staticmethod
    def valid_audio_file(file_name: str) -> bool:
        """
        :param file_name: The name of the file.
        :return: If the file is a valid audio file based on its extension.
        """

        return file_name.endswith('.mp3') \
               or file_name.endswith('.wav') \
               or file_name.endswith('.ogg')

    def __init__(self, audio_dir: Path = Path('reminder-audio/')):
        """
        Initializes the folder with the audio files.

        :param audio_dir: The Path to the directory that contains audio files.
        """

        self.audio_dir = audio_dir

    def get_available_audio_files(self) -> [Path, ]:
        """
        :return: All available audio files in the audio file directory.
        """

        return list(filter(lambda name: Audio.valid_audio_file(name),
                           [file_name for file_name in listdir(self.audio_dir)]))

    def get_random_audio_file(self) -> Path or None:
        """
        :return: A random audio file inside of the audio folder or None if unable to retrieve an audio file.
        """

        audio_files: [Path, ] = self.get_available_audio_files()

        if len(audio_files) == 0:
            return None
        elif len(audio_files) == 1:
            return Path(self.audio_dir, audio_files[0])
        else:
            return Path(self.audio_dir, audio_files[randint(0, len(audio_files) - 1)])

    def play_random_audio(self) -> None:
        """
        Retrieves a random audio file from the audio directory and plays it.
        """

        # Convert the Path object into an absolute Path string.
        rand_audio_file: str = self.get_random_audio_file().absolute().as_posix()

        if rand_audio_file is None:
            print(f'Unable to find an audio file to play in {self.audio_dir.name}')
        else:
            playsound(rand_audio_file)

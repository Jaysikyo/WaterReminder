"""
Main script for the project that runs the program from start to finish.

:author: Jacob Singleton
"""

from pathlib import Path
from random import randint
from time import sleep
from audio import Audio
from config import Config


def show_startup_banner() -> None:
    """
    Displays an ASCII art startup banner explaining the program.
    """

    print(
        '+------------------------------------------------------------------+',
        '|                          Water Reminder                          |',
        '+------------------------------------------------------------------+',
        '',
        'This program is designed to periodically remind you to drink water.',
        'Water is the source of all life and is vital to living well!',
        '',
        'An audio segment will play to remind you to drink water periodically.',
        '',
        'Head to the \'config.yml\' file to configure this program to your needs.',
        'To add more sounds, simply put audio files into the audio directory!',
        '',
        '----------------------------------------------------------------------',
        '',
        sep='\n'
    )


def water_reminder_loop(audio_player: Audio, config: Config) -> None:
    """
    Main loop of the program that periodically plays water reminding audio files.

    :param audio_player: The Audio object for playing the water reminding audio files.
    :param config: The configuration variables for the program.
    """

    while True:
        sleep(randint(config.min_interval, config.max_interval) * 60)

        audio_player.play_random_audio()


if __name__ == '__main__':
    show_startup_banner()

    config: Config = Config(Path('config.yml'))
    audio_player = Audio(config.audio_path)

    audio_player.play_random_audio()
    water_reminder_loop(audio_player, config)

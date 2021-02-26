"""
Unit Testing for the Audio class.

:author: Jacob Singleton
"""


import unittest
from audio import Audio
from pathlib import Path


class AudioTest(unittest.TestCase):
    def test_valid_audio_file_name(self):
        self.assertTrue(Audio.valid_audio_file('sound.mp3'))
        self.assertTrue(Audio.valid_audio_file('byte.wav'))
        self.assertTrue(Audio.valid_audio_file('bit.ogg'))

        self.assertFalse(Audio.valid_audio_file('sound'))
        self.assertFalse(Audio.valid_audio_file('byte.m4a'))
        self.assertFalse(Audio.valid_audio_file('bitmp3'))

    def test_getting_all_available_audio_files(self):
        audio_player = Audio(Path('test/audio'))
        audio_files: {Path, } = set(audio_player.get_available_audio_files())

        self.assertEqual(len(audio_files), 2)
        self.assertEqual(audio_files, {'audio-1.mp3', 'audio-2.mp3'})

    def test_getting_random_audio_from_empty_directory_returns_none(self):
        audio_player = Audio(Path('test/audio-empty'))

        self.assertIsNone(audio_player.get_random_audio_file())

    def test_getting_random_audio_from_singleton_directory(self):
        audio_player = Audio(Path('test/audio-single'))

        self.assertIsNotNone(audio_player.get_random_audio_file())


if __name__ == '__main__':
    unittest.main()

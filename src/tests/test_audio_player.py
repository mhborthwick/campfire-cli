import pytest
import pygame
from src.main import AudioPlayer


@pytest.fixture
def audio_player():
    return AudioPlayer()


def test_initialize(audio_player, mocker):
    sound_file = "path/to/sound.mp3"
    mocker.patch('pygame.mixer.init')
    mocker.patch('pygame.mixer.music.load')
    mocker.patch('pygame.mixer.music.set_volume')
    audio_player.initialize(sound_file)
    pygame.mixer.init.assert_called_once()
    pygame.mixer.music.load.assert_called_once_with(sound_file)
    pygame.mixer.music.set_volume.assert_called_once_with(0.8)


def test_play_audio(audio_player, mocker):
    mocker.patch('pygame.mixer.music.play')
    audio_player.play()
    pygame.mixer.music.play.assert_called_once_with(loops=-1)


def test_stop_audio(audio_player, mocker):
    mocker.patch('pygame.mixer.music.stop')
    audio_player.stop()
    pygame.mixer.music.stop.assert_called_once()


def test_get_sound_file_path(audio_player, mocker):
    mocker.patch('os.path.abspath', return_value="/path/to/my/script")
    mocker.patch('os.path.dirname', return_value="/path/to/my")
    file_path = audio_player.get_sound_file_path()
    assert file_path == '/path/to/my/audio/campfire_sound.mp3'

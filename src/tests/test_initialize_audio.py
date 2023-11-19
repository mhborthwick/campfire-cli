import pytest
from src.main import initialize_audio


@pytest.fixture
def initialize_audio_mock(mocker):
    return mocker.patch('pygame.mixer.init'), mocker.patch('pygame.mixer.music.load'), mocker.patch('pygame.mixer.music.set_volume')


def test_initialize_audio(initialize_audio_mock):
    sound_file = 'path/to/audio/file.mp3'
    initialize_audio(sound_file)
    initialize_audio_mock[0].assert_called_once()
    initialize_audio_mock[1].assert_called_once_with(sound_file)
    initialize_audio_mock[2].assert_called_once_with(0.5)

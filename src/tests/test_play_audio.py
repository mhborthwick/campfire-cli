import pytest
from src.main import play_audio


@pytest.fixture
def play_audio_mock(mocker):
    return mocker.patch('pygame.mixer.music.play')


def test_play_audio(play_audio_mock):
    play_audio()
    play_audio_mock.assert_called_once_with(loops=-1)

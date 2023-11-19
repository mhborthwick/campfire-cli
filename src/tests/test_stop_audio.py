import pytest
from src.main import stop_audio


@pytest.fixture
def stop_audio_mock(mocker):
    return mocker.patch('pygame.mixer.music.stop')


def test_play_audio(stop_audio_mock):
    stop_audio()
    stop_audio_mock.assert_called_once()

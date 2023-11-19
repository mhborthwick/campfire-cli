import pytest
from src.main import play_audio


@pytest.fixture
def pygame_mock(mocker):
    return mocker.patch('pygame.mixer.music.play')


def test_play_audio(pygame_mock):
    play_audio()
    pygame_mock.assert_called_once_with(loops=-1)

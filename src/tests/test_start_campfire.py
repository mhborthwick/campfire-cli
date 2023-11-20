import pytest
from typer.testing import CliRunner
from unittest.mock import patch, MagicMock
from src.main import app


@pytest.fixture
def audio_player_mock(mocker):
    return mocker.patch('src.main.AudioPlayer')


@pytest.fixture
def campfire_printer_mock(mocker):
    return mocker.patch('src.main.CampfirePrinter')


@pytest.fixture
def cli_runner():
    return CliRunner()


def test_start_campfire(cli_runner, audio_player_mock, campfire_printer_mock, mocker):
    with patch('src.main.console', MagicMock(name='Console')) as console_mock:
        result = cli_runner.invoke(app, ["--sound", "--verbose"])
        assert result.exit_code == 0
        audio_player_mock_instance = audio_player_mock.return_value
        campfire_printer_mock_instance = campfire_printer_mock.return_value
        audio_player_mock.assert_called_once()
        campfire_printer_mock.assert_called_once_with(
            console_mock, audio_player_mock_instance)
        campfire_printer_mock_instance.print_campfire.assert_called_once_with(
            mocker.ANY,
            sound=True,
            verbose=True
        )

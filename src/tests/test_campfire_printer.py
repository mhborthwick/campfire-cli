import pytest
from src.main import CampfirePrinter


@pytest.fixture
def console_mock(mocker):
    return mocker.patch('rich.console.Console')


@pytest.fixture
def audio_player_mock(mocker):
    return mocker.patch('src.main.AudioPlayer')


@pytest.fixture
def campfire_printer(console_mock, audio_player_mock):
    return CampfirePrinter(console_mock, audio_player_mock)


def test_print_frame(console_mock, campfire_printer):
    frame = [
        "    , , , `   ",
        "     ` , ,    ",
        "      , ,     ",
        "     , , ,    ",
        "    , , , ,   ",
    ]
    campfire_printer.print_frame(frame)
    assert console_mock.print.call_count == len(frame) + 2


def test_print_campfire(console_mock, audio_player_mock, campfire_printer, mocker):
    frames = [
        ["frame1"],
        ["frame2"],
    ]
    mocker.patch('time.sleep')
    campfire_printer.stop_campfire()  # stop loop during testing
    campfire_printer.print_campfire(frames, True, True)
    console_mock.clear.assert_called()
    console_mock.print.assert_called()
    audio_player_mock.initialize.assert_called_once()
    audio_player_mock.play.assert_called_once()
    audio_player_mock.stop.assert_called_once()


def test_print_campfire_no_sound(console_mock, audio_player_mock, campfire_printer, mocker):
    frames = [
        ["frame1"],
        ["frame2"],
    ]
    mocker.patch('time.sleep')
    campfire_printer.stop_campfire()  # stop loop during testing
    campfire_printer.print_campfire(frames, False, True)
    console_mock.clear.assert_called()
    console_mock.print.assert_called()
    audio_player_mock.initialize.assert_not_called()
    audio_player_mock.play.assert_not_called()
    audio_player_mock.stop.assert_not_called()

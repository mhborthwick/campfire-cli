import os
import typer
import time
import pygame
from rich.console import Console

app = typer.Typer()

console = Console()

rocks = "[bold grey50] (( )( )( )( )) [/bold grey50]"
grass = "[bold medium_spring_green] `````````````` [/bold medium_spring_green]"


class AudioPlayer:
    def initialize(self, sound_file):
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.set_volume(0.5)

    def play(self):
        pygame.mixer.music.play(loops=-1)

    def stop(self):
        pygame.mixer.music.stop()

    def get_audio_path(self):
        script_path = os.path.abspath(__file__)
        script_dir = os.path.dirname(script_path)
        return os.path.join(script_dir, "audio", "campfire_sound.mp3")


class CampfirePrinter:
    def __init__(self, console, audio_player):
        self.console = console
        self.audio_player = audio_player

    def print_frame(self, frame):
        for i, line in enumerate(frame):
            sway = " " * (i % 2)
            colored_line = (
                "[bold red]" + sway + line[:5] + "[/bold red]" +
                "[bold yellow]" + line[5:] + "[/bold yellow]"
            )
            self.console.print(colored_line)
        self.console.print(rocks)
        self.console.print(grass)

    def print_campfire(self, frames, sound, verbose):
        try:
            if sound:
                audio_path = self.audio_player.get_audio_path()
                self.audio_player.initialize(audio_path)
                self.audio_player.play()
            while True:
                for frame in frames:
                    self.console.clear()
                    self.print_frame(frame)
                    if verbose:
                        self.console.print(f'sound={sound}')
                    self.console.print()
                    time.sleep(0.2)
        except KeyboardInterrupt:
            if sound:
                self.audio_player.stop()
            self.console.print("[bold]Campfire animation stopped![/bold]")


@app.command()
def start_campfire(
        sound: bool = typer.Option(False, help="Enable campfire sound"),
        verbose: bool = typer.Option(True, help="Display campfire sound on/off message")):
    audio_player = AudioPlayer()
    campfire_printer = CampfirePrinter(console, audio_player)
    campfire_frames = [
        [
            "    , , , `   ",
            "     ` , ,    ",
            "      , ,     ",
            "     , , ,    ",
            "    , , , ,   ",
        ],
        [
            "     ` , ,    ",
            "      , `     ",
            "     , , ,    ",
            "    , , , ,   ",
            "   , , , , ,  ",
        ],
        [
            "      , `     ",
            "     ` , ,    ",
            "    , , , ,   ",
            "   , , , , ,  ",
            "  , , , , , , ",
        ],
        [
            "     ` , ,    ",
            "    , , , `   ",
            "   , , , , ,  ",
            "  , , , , , , ",
            " , , , , , , ,",
        ],
    ]
    campfire_printer.print_campfire(
        campfire_frames, sound=sound, verbose=verbose)


if __name__ == "__main__":
    app()

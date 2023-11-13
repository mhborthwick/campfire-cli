import os
import typer
import time
import pygame
from rich import print
from rich.console import Console


app = typer.Typer()

console = Console()

rocks = "[bold grey50] (( )( )( )( )) [/bold grey50]"
grass = "[bold medium_spring_green] `````````````` [/bold medium_spring_green]"


def initialize_audio(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.set_volume(0.5)


def play_audio():
    pygame.mixer.music.play(loops=-1)


def stop_audio():
    pygame.mixer.music.stop()


def print_campfire(frames: list[list[str]], sound=False, verbose=True):
    if sound:
        script_path = os.path.abspath(__file__)
        script_dir = os.path.dirname(script_path)
        audio_path = os.path.join(script_dir, "audio", "campfire_sound.mp3")
        initialize_audio(audio_path)
        play_audio()
    try:
        while True:
            for frame in frames:
                console.clear()
                for i, line in enumerate(frame):
                    sway = " " * (i % 2)
                    colored_line = (
                        "[bold red]" + sway + line[:5] + "[/bold red]" +
                        "[bold yellow]" + line[5:] + "[/bold yellow]"
                    )
                    print(colored_line)
                print(rocks)
                print(grass)
                if verbose:
                    print(f'sound={sound}')
                print()
                time.sleep(0.2)
    except KeyboardInterrupt:
        if sound:
            stop_audio()
        console.print("[bold]Campfire animation stopped![/bold]")


@app.command()
def start_campfire(
        sound: bool = typer.Option(False, help="Enable campfire sound"),
        verbose: bool = typer.Option(True, help="Display campfire sound on/off message")):
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
    print_campfire(campfire_frames, sound=sound, verbose=verbose)


if __name__ == "__main__":
    app()

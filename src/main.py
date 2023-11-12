import typer
import time
from rich import print
from rich.console import Console

app = typer.Typer()

console = Console()

rocks_lower = "[bold grey50] (( )( )( )( )) [/bold grey50]"
grass = "[bold medium_spring_green] `````````````` [/bold medium_spring_green]"


def print_campfire(frames: list[list[str]]):
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
                print(rocks_lower)
                print(grass)
                print()
                time.sleep(0.2)
    except KeyboardInterrupt:
        console.print("[bold]Campfire animation stopped![/bold]")


@app.command()
def start_campfire():
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
    print_campfire(campfire_frames)


if __name__ == "__main__":
    app()

import typer
import time
from rich import print
from rich.console import Console

app = typer.Typer()

console = Console()


def print_campfire():
    campfire_frames = [
        [
            "    , , , ,   ",
            "     , , ,    ",
            "      , ,     ",
            "     , , ,    ",
            "    , , , ,   ",
        ],
        [
            "     , , ,    ",
            "      , ,     ",
            "     , , ,    ",
            "    , , , ,   ",
            "   , , , , ,  ",
        ],
        [
            "      , ,     ",
            "     , , ,    ",
            "    , , , ,   ",
            "   , , , , ,  ",
            "  , , , , , , ",
        ],
        [
            "     , , ,    ",
            "    , , , ,   ",
            "   , , , , ,  ",
            "  , , , , , , ",
            " , , , , , , ,",
        ],
    ]
    try:
        while True:
            for frame in campfire_frames:
                console.clear()
                for line in frame:
                    colored_line = (
                        "[bold red]" + line[:5] + "[/bold red]" +
                        "[bold yellow]" + line[5:] + "[/bold yellow]"
                    )
                    print(colored_line)
                print()
                time.sleep(0.2)
    except KeyboardInterrupt:
        console.print("[bold]Campfire animation stopped![/bold]")


@app.command()
def start_campfire():
    print_campfire()


if __name__ == "__main__":
    app()

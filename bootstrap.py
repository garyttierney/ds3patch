from os import getenv
from pathlib import Path

from soulstruct.darksouls3.events import *

UNPACKED_GAME_PATH = Path(getenv("GAME_PATH"))


def unpack_events():
    event_files = UNPACKED_GAME_PATH.glob('event/*.emevd.dcx')

    for event_file in event_files:
        try:
            event = EMEVD(event_file)
            out_path = (Path("src/event/") / event_file.name)

            """
            Strip off the .emevd.dcx if present, which counts as multiple suffixes.
            """
            while out_path.suffix != '':
                out_path = out_path.with_suffix('')

            event.write_evs(out_path.with_suffix('.py'))
        except Exception:
            print(event_file)
            pass


def bootstrap():
    unpack_events()


if __name__ == '__main__':
    bootstrap()

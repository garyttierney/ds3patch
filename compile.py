import argparse

from soulstruct.darksouls3.events import EMEVD


def compile_evs(input: str, output: str):
    example_emevd = EMEVD(input)
    example_emevd.write(output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", help="Path to the input EVS python file", required=True)
    parser.add_argument("--output", help="Path to write the output EMEVD.DCX file", required=True)
    args = parser.parse_args()

    compile_evs(args.source, args.output)

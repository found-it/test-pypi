import argparse

from foundit_hello.greeter import Hello


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="hello", description="Greet someone.")
    parser.add_argument("name", nargs="?", default="world")
    parser.add_argument("-e", "--excited", action="store_true")
    args = parser.parse_args(argv)

    print(Hello(name=args.name, excited=args.excited).greet())
    return 0

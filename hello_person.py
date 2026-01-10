"""
hello_person.py - A small CLI with argparse.

Learning goals:
- Build a command-line interface
- Use dictionaries to map language codes to greetings
- Handle defaults and invalid input
"""

import argparse


GREETINGS = {
    "en": "Hello",
    "es": "Hola",
    "fr": "Bonjour",
    "de": "Hallo",
    "it": "Ciao",
}


def hello(name, lang="en"):
    greeting = GREETINGS.get(lang, GREETINGS["en"])
    return f"{greeting}, {name}!"


def parse_args():
    parser = argparse.ArgumentParser(description="Greet a person.")
    parser.add_argument(
        "-n",
        "--name",
        required=True,
        help="Name of the person to greet",
    )
    parser.add_argument(
        "-l",
        "--lang",
        default="en",
        choices=sorted(GREETINGS.keys()),
        help="Language for the greeting",
    )
    return parser.parse_args()


NOTES = """
Notes:
- argparse validates inputs and prints helpful usage errors.
- choices limits allowed values; defaults keep the CLI friendly.
"""


QUESTIONS = """
Questions:
1) What happens if you omit the --name argument?
2) How would you add a new language to the GREETINGS dict?
3) Why might you want to separate parse_args from hello?
4) How would you make --lang optional with a default?
"""


def main():
    args = parse_args()
    print(hello(args.name, args.lang))
    print(NOTES.strip())
    print()
    print(QUESTIONS.strip())


if __name__ == "__main__":
    main()

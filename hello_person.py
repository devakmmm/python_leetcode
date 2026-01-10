"""
hello_person.py - A small CLI with argparse.

Learning goals:
- Build a command-line interface
- Use dictionaries to map language codes to greetings
- Handle defaults and invalid input
"""

import argparse  # Import argparse for command-line parsing.


GREETINGS = {  # Map language codes to greeting words.
    "en": "Hello",  # English greeting.
    "es": "Hola",  # Spanish greeting.
    "fr": "Bonjour",  # French greeting.
    "de": "Hallo",  # German greeting.
    "it": "Ciao",  # Italian greeting.
}  # End the greetings map.


def hello(name, lang="en"):  # Define a greeting function with a language code.
    greeting = GREETINGS.get(lang, GREETINGS["en"])  # Resolve the greeting text.
    return f"{greeting}, {name}!"  # Build and return the greeting.


EXAMPLE_WALKTHROUGH_HELLO = """  # Store a walkthrough for hello.
Example Walkthrough: hello
- greeting = GREETINGS.get(lang, GREETINGS["en"]):
  looks up the greeting for the language code, defaults to English.
- return f"{greeting}, {name}!":
  returns a greeting string.
Example usage:
- hello("Dave", "fr") returns "Bonjour, Dave!"
"""


def parse_args():  # Define a function to parse CLI arguments.
    parser = argparse.ArgumentParser(description="Greet a person.")  # Create a parser.
    parser.add_argument(  # Add the name argument.
        "-n",  # Short flag for name.
        "--name",  # Long flag for name.
        required=True,  # Require a name value.
        help="Name of the person to greet",  # Describe the argument.
    )  # End the name argument definition.
    parser.add_argument(  # Add the language argument.
        "-l",  # Short flag for language.
        "--lang",  # Long flag for language.
        default="en",  # Provide a default language.
        choices=sorted(GREETINGS.keys()),  # Restrict values to known codes.
        help="Language for the greeting",  # Describe the argument.
    )  # End the language argument definition.
    return parser.parse_args()  # Parse and return the CLI arguments.


EXAMPLE_WALKTHROUGH_PARSE_ARGS = """  # Store a walkthrough for parse_args.
Example Walkthrough: parse_args
- parser = argparse.ArgumentParser(...):
  creates an argument parser with a description.
- parser.add_argument("-n", "--name", required=True, ...):
  defines a required name argument.
- parser.add_argument("-l", "--lang", default="en", choices=...):
  defines an optional language argument.
- return parser.parse_args():
  reads CLI arguments and returns a namespace.
Example usage:
- python3 hello_person.py -n Dave -l es
  results in args.name="Dave", args.lang="es".
"""


NOTES = """  # Store study notes as a multiline string.
Notes:
- argparse validates inputs and prints helpful usage errors.
- choices limits allowed values; defaults keep the CLI friendly.
"""


QUESTIONS = """  # Store practice questions as a multiline string.
Questions:
1) What happens if you omit the --name argument?
2) How would you add a new language to the GREETINGS dict?
3) Why might you want to separate parse_args from hello?
4) How would you make --lang optional with a default?
"""


def main():  # Define the script entry point.
    args = parse_args()  # Parse command-line arguments.
    print(hello(args.name, args.lang))  # Print the greeting.
    print(NOTES.strip())  # Print notes without extra whitespace.
    print()  # Print a blank line between notes and questions.
    print(QUESTIONS.strip())  # Print questions for review.


EXAMPLE_WALKTHROUGH_MAIN = """  # Store a walkthrough for main.
Example Walkthrough: main
- args = parse_args():
  reads the CLI inputs.
- print(hello(args.name, args.lang)):
  prints the greeting for the chosen language.
- print(NOTES.strip()):
  prints the Notes block.
- print():
  prints a blank line.
- print(QUESTIONS.strip()):
  prints the Questions block.
"""


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.

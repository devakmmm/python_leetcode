def hello(name, lang):
    greetings = {
        "en": "Hello",
        "es": "Hola",
        "fr": "Bonjour",
        "de": "Hallo",
        "it": "Ciao"
    }

    msg= f"{greetings[lang]}, {name}!"
    print(msg)

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description="Greet a person.")

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="Name of the person to greet"
    )

    parser.add_argument(
        "-l", "--lang", metavar="lang",
        default="en", choices=["en", "es", "fr", "de", "it"],
        help="Language for the greeting (default: en)"
    )

    args = parser.parse_args()

    msg = f"Hello, {args.name}!"

    print(msg)
    # This code uses argparse to create a command-line interface that requires a name argument.
    # The name provided by the user is then used in an f-string to format a greeting message.
    # F-strings allow for easy and readable string formatting, making it simple to include variables in strings.
    # The argparse module is used to handle command-line arguments, making the script flexible and user-friendly.
    # The output will display a personalized greeting based on the name provided by the user.
    # Example usage: python hello_person.py -n Dave
    # Output: Hello, Dave!
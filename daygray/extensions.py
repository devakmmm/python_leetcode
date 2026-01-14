"""
extensions.py - Working with file extensions using pathlib.

Learning goals:
- Extract file extensions
- Work with stems and suffixes
- Build new paths safely
"""

from pathlib import Path  # Import Path for filesystem path handling.


def show_section(title):  # Define a helper to label output sections.
    print("\n" + title)  # Print a blank line and the section title.
    print("-" * len(title))  # Print a dashed underline under the title.


def extension_examples():  # Define a demo for extension inspection.
    show_section("File extensions")  # Display the section header.
    paths = [  # Create a list of example paths.
        Path("report.pdf"),  # Add a file with one extension.
        Path("archive.tar.gz"),  # Add a file with multiple extensions.
        Path("photo.jpeg"),  # Add a file with a single extension.
        Path(".env"),  # Add a hidden file with no suffix.
        Path("README"),  # Add a file without an extension.
    ]  # End the list of paths.

    for p in paths:  # Loop over each path.
        print("path:", p, "suffix:", p.suffix, "suffixes:", p.suffixes, "stem:", p.stem)  # Show parts.


EXAMPLE_WALKTHROUGH_EXTENSION = """  # Store a walkthrough for extension_examples.
Example Walkthrough: extension_examples
- show_section("File extensions"):
  prints the section header.
- paths = [Path("report.pdf"), Path("archive.tar.gz"), ...]:
  creates Path objects with different suffix patterns.
- for p in paths:
  iterates over each Path.
- print(...):
  prints the path, suffix, suffixes, and stem for each.
Example output line:
- path: report.pdf suffix: .pdf suffixes: ['.pdf'] stem: report
"""


def build_paths():  # Define a demo for building paths.
    show_section("Building paths")  # Display the section header.
    base = Path("projects") / "demo"  # Join path components safely.
    file_path = base / "data.csv"  # Build a file path under the base.
    print("base:", base)  # Print the base path.
    print("file:", file_path)  # Print the file path.
    print("with different suffix:", file_path.with_suffix(".json"))  # Change extension.


EXAMPLE_WALKTHROUGH_BUILD = """  # Store a walkthrough for build_paths.
Example Walkthrough: build_paths
- show_section("Building paths"):
  prints the section header.
- base = Path("projects") / "demo":
  builds a path like projects/demo.
- file_path = base / "data.csv":
  builds a path like projects/demo/data.csv.
- print("base:", base):
  outputs: base: projects/demo
- print("file:", file_path):
  outputs: file: projects/demo/data.csv
- print("with different suffix:", file_path.with_suffix(".json")):
  outputs: with different suffix: projects/demo/data.json
"""


NOTES = """  # Store study notes as a multiline string.
Notes:
- pathlib handles paths in an OS-agnostic way.
- Path.suffix returns the last extension; Path.suffixes returns all.
- Hidden files like .env have no suffix because there is no stem.
"""


QUESTIONS = """  # Store practice questions as a multiline string.
Questions:
1) What is the difference between suffix and suffixes?
2) How would you change "archive.tar.gz" to "archive.zip"?
3) Why is using pathlib safer than string concatenation?
"""


def main():  # Define the script entry point.
    extension_examples()  # Run the extension examples.
    build_paths()  # Run the path building examples.
    print(NOTES.strip())  # Print notes without extra whitespace.
    print()  # Print a blank line between notes and questions.
    print(QUESTIONS.strip())  # Print questions for review.


EXAMPLE_WALKTHROUGH_MAIN = """  # Store a walkthrough for main.
Example Walkthrough: main
- extension_examples():
  runs the file extension section.
- build_paths():
  runs the path building section.
- print(NOTES.strip()):
  prints the Notes block.
- print():
  prints a blank line.
- print(QUESTIONS.strip()):
  prints the Questions block.
"""


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.

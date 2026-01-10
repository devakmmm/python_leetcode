"""
extensions.py - Working with file extensions using pathlib.

Learning goals:
- Extract file extensions
- Work with stems and suffixes
- Build new paths safely
"""

from pathlib import Path


def show_section(title):
    print("\n" + title)
    print("-" * len(title))


def extension_examples():
    show_section("File extensions")
    paths = [
        Path("report.pdf"),
        Path("archive.tar.gz"),
        Path("photo.jpeg"),
        Path(".env"),
        Path("README"),
    ]

    for p in paths:
        print("path:", p, "suffix:", p.suffix, "suffixes:", p.suffixes, "stem:", p.stem)


def build_paths():
    show_section("Building paths")
    base = Path("projects") / "demo"
    file_path = base / "data.csv"
    print("base:", base)
    print("file:", file_path)
    print("with different suffix:", file_path.with_suffix(".json"))


NOTES = """
Notes:
- pathlib handles paths in an OS-agnostic way.
- Path.suffix returns the last extension; Path.suffixes returns all.
- Hidden files like .env have no suffix because there is no stem.
"""


QUESTIONS = """
Questions:
1) What is the difference between suffix and suffixes?
2) How would you change "archive.tar.gz" to "archive.zip"?
3) Why is using pathlib safer than string concatenation?
"""


def main():
    extension_examples()
    build_paths()
    print(NOTES.strip())
    print()
    print(QUESTIONS.strip())


if __name__ == "__main__":
    main()

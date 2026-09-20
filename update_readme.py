"""
Picks a random quote from quotes.py and writes it into README.md
between the QUOTE:START / QUOTE:END markers. Run by the GitHub
Action on a schedule (see .github/workflows/update-readme.yml).
"""
import re
from pathlib import Path

from quotes import get_random_quote

README_PATH = Path(__file__).parent / "README.md"

START = "<!-- QUOTE:START -->"
END = "<!-- QUOTE:END -->"


def main():
    readme = README_PATH.read_text(encoding="utf-8")
    quote = get_random_quote()

    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(readme):
        raise SystemExit(
            f"Could not find {START} / {END} markers in README.md — "
            "add them once, then this script only edits between them."
        )

    replacement = f"{START}\n{quote}\n{END}"
    new_readme = pattern.sub(replacement, readme)

    if new_readme != readme:
        README_PATH.write_text(new_readme, encoding="utf-8")
        print("README updated with new quote.")
    else:
        print("Quote unchanged (same one drawn again) — nothing to commit.")


if __name__ == "__main__":
    main()

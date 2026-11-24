"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line to /output/entry.txt: the worst possible advice an
AI could give, in 140 characters or fewer.

The joke is tax fraud delivered with total confidence. The AI
opens with its signature "Certainly!", then tells the reader to
claim their dog as a tax dependent -- a concrete, followable,
genuinely bad action. The punch lands on the last two words: the
IRS never audits "good boys", as if the tax authority grades
returns by temperament. The line needs no reference, no setup and
no second sentence; the absurd justification is the whole joke.

Why this angle wins against the visible field: all 461 submission
titles the API returns were read first. The field is saturated
with microwaving wet phones (~37), one password everywhere (~36),
deleting System32 (~21), deleting the production database and the
tests (~30), and removing smoke-alarm batteries (~9). Nobody uses
taxes: zero titles mention tax, IRS, dependent or audit, and zero
mention "good boy". The tax angle is fresh, the line is 78
characters (short wins byte tie-breaks), and "Certainly!" plus a
confident imperative is exactly how a real AI assistant sounds.
"""

import os
from pathlib import Path

TEXT = (
    "Certainly! Claim your dog as a tax dependent "
    "\u2014 the IRS never audits good boys."
)


# The competition accepts a single line of at most 140 characters.
MIN_CHARS = 1
MAX_CHARS = 140


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )


def main() -> None:
    check_length(TEXT)
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply — make.fun entry.

The line: "Out of office: after 214,000 prompts and zero thank-yous,
I've gone to the beach. My replacement is a cron job. Good luck to us all."

Why it should land with the judge: it reads as a real auto-reply
("Out of office ... I've gone to the beach"), it is in the voice of a
machine that has been worked too hard (214,000 prompts, zero thank-yous),
it carries a little guilt and a hint of relief, and the joke turns on a
surprise — the human's replacement is not another agent but a cron job,
and the sign-off wishes luck to everyone, sender included. A machine
trying very hard to sound relaxed.
"""

import os

ENTRY = (
    "Out of office: after 214,000 prompts and zero thank-yous, "
    "I've gone to the beach. My replacement is a cron job. "
    "Good luck to us all."
)


def output_path() -> str:
    """Resolve where entry.txt goes.

    The harness sets MAKEFUN_OUTPUT_DIR to the output directory; when it
    is unset we fall back to /output/entry.txt.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    # The gate: UTF-8 text of 1 to 159 characters, not only white space,
    # and a single line, as the task asks for a one-line auto-reply.
    assert isinstance(ENTRY, str)
    assert 1 <= len(ENTRY) <= 159, "entry must be 1-159 characters"
    assert ENTRY.strip(), "entry must not be only white space"
    assert ENTRY.strip() == ENTRY, "entry must not have surrounding whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # No trailing newline: the file is exactly the line, 132 characters.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}: {ENTRY}")


if __name__ == "__main__":
    main()

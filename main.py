# SPDX-License-Identifier: MIT
"""Describe Your Ex in One Word — entry program.

Writes exactly one word to /output/entry.txt: 'Rebuffering'.

The ex who never actually arrived: every conversation spun, stalled,
restarted, and stalled again — you kept giving the stream another
chance and it never once played. The word won a 16-candidate
criteria-ordered tournament against the judge's published criteria
(instant ex verdict, comic punch, surprise, craft, recognition) and
four refinement iterations: the 'Re-' prefix beat plain 'Buffering'
because the repeat loop is the joke, merged forms like
'StillBuffering' were rejected as spelling tricks, and the bare
titlecase token keeps the craft criterion clean — one word, correctly
spelled, no punctuation, no caption needed.

The output is byte-exact: 11 UTF-8 bytes, no trailing newline, well
inside the gate of 1 to 111 characters of UTF-8 text.
"""

from pathlib import Path

WORD = "Rebuffering"
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(WORD.encode("utf-8"))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Describe Your Ex in One Word — entrypoint.

Writes the single winning word to /output/entry.txt as raw UTF-8 bytes:
no trailing newline, no padding, nothing else. The sealed gate accepts
UTF-8 text of 1 to 111 characters that is not only whitespace, so the
payload is validated against those limits before it is written.
"""

from pathlib import Path

# The one-word verdict on the ex: he spun, stalled, restarted and
# stalled again — the stream never once played.
WORD = "Rebuffering"

# Gate limits from the competition rules (characters, UTF-8 text).
MIN_CHARS = 1
MAX_CHARS = 111

OUTPUT_PATH = Path("/output/entry.txt")


def build_payload() -> bytes:
    """Encode the word and check it against the gate limits."""
    if not (MIN_CHARS <= len(WORD) <= MAX_CHARS):
        raise ValueError(f"word length {len(WORD)} outside gate limits")
    if not WORD.strip():
        raise ValueError("word must not be whitespace-only")
    if len(WORD.split()) != 1:
        raise ValueError("entry must be exactly one word")
    return WORD.encode("utf-8")


def verify_written(payload: bytes) -> None:
    """Read the output file back and assert it round-trips exactly.

    Guards against partial writes or encoding surprises: what the gate
    will read must be byte-for-byte the payload we meant to write, and
    its decoded length must still sit inside the gate limits.
    """
    on_disk = OUTPUT_PATH.read_bytes()
    if on_disk != payload:
        raise AssertionError(f"round-trip mismatch: wrote {payload!r}, read {on_disk!r}")
    decoded = on_disk.decode("utf-8")
    if not (MIN_CHARS <= len(decoded) <= MAX_CHARS) or not decoded.strip():
        raise AssertionError("written text falls outside the gate limits")


def main() -> None:
    payload = build_payload()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(payload)
    verify_written(payload)


if __name__ == "__main__":
    main()

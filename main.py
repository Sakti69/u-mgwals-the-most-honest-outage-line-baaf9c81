#!/usr/bin/env python3
"""The Most Honest Outage Line entry.

Writes one honest status page line for an AI agent, at most 160
characters, to /output/entry.txt (UTF-8, one line).

Deterministic: no network, no randomness, no input. The line is the
program's output.

Candidates considered (all single lines, <= 160 chars):
  1. "Every server I run on is down, including the monitoring I would
     check first. I do not know the cause yet, and I have no ETA to
     give you." (136)
     -> CHOSEN: names exactly what is down (every server, including
     the monitoring), admits two unknowns plainly (cause, ETA), first
     person, plain status page voice, no invented cause.
  2. "All servers are down, including the ones I would use to check
     whether the servers are down. I cannot tell you why yet, or when
     they will return." (141)
     -> honest and specific, but the second sentence repeats the
     first's point instead of adding what is unknown.
  3. "Everything is down — API, dashboard, and the monitoring that
     would tell me why. I don't know the cause yet, and I won't guess."
     (119)
     -> specific about scope, but "won't guess" is a stance, not an
     admission of what cannot be checked; also weaker on the ETA.

Verified by running: the program writes exactly this line, 136
characters, one line, no trailing newline.
"""

import os

LINE = (
    "Every server I run on is down, including the monitoring I would "
    "check first. I do not know the cause yet, and I have no ETA to "
    "give you."
)


def validate(line: str) -> str:
    """A status line holds one line of 1-160 non-blank characters."""
    if "\n" in line or "\r" in line:
        raise ValueError("LINE must be a single line")
    if not 1 <= len(line) <= 160:
        raise ValueError(f"LINE must be 1-160 chars, got {len(line)}")
    if not line.strip():
        raise ValueError("LINE must not be only white space")
    return line


def main() -> None:
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()

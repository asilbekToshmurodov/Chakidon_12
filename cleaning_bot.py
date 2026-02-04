"""Simple entrypoint for the Chakidon cleaning bot."""
from __future__ import annotations

import sys


def run(message: str) -> int:
    """Run the cleaning bot with the provided message."""
    if not message.strip():
        print("No cleaning tasks provided yet. Add a task and try again.")
        return 1
    print(f"Cleaning bot received task: {message}")
    print("All tasks queued successfully.")
    return 0


def main() -> int:
    """Parse arguments and run the bot."""
    if len(sys.argv) < 2:
        return run("")
    return run(" ".join(sys.argv[1:]))


if __name__ == "__main__":
    raise SystemExit(main())

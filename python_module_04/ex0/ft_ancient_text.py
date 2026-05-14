import sys
from typing import List


def recover_anxient_text(args: List[str]) -> None:
    """
    Reads a file specified in command line arguments and prints its content.
    Handles file-related exceptions and ensures the file is closed.
    """
    if len(args) != 2:
        print(f"Usage: {args[0]} <file>")
        return

    file_path: str = args[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_path}'")

    file_handle = None
    try:
        file_handle = open(file_path, 'r')
        print("---")
        content: str = file_handle.read()
        print(content, end="" if content.endswith("\n") else "\n")
        print("---")

    except Exception as e:
        print(f"Error opening file '{file_path}': {e}")

    finally:
        if file_handle is not None:
            file_handle.close()
            print(f"File '{file_path}' closed.")


if __name__ == "__main__":
    recover_anxient_text(sys.argv)

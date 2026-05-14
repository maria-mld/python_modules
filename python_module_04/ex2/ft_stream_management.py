import sys
from typing import List


def process_streams(args: List[str]) -> None:
    """
    Reads, transforms, and saves archive data using low-level streams.
    Directly uses sys.stdin for input and sys.stderr for errors.
    """
    if len(args) != 2:
        sys.stdout.write(f"Usage: {args[0]} <file>\n")
        return

    file_path: str = args[1]
    sys.stdout.write("=== Cyber Archives Recovery & Preserveration ===\n")
    sys.stdout.write(f"Accessing file '{file_path}'\n")

    original_content: str = ""
    file_handle = None

    try:
        file_handle = open(file_path, 'r')
        original_content = file_handle.read()
        sys.stdout.write("---\n")
        sys.stdout.write(original_content)
        if not original_content.endswith("\n"):
            sys.stdout.write("\n")
        sys.stdout.write("---\n")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{file_path}': {e}\n")
        return
    finally:
        if file_handle is not None:
            file_handle.close()
            sys.stdout.write(f"File '{file_path}' closed.\n")

    sys.stdout.write("Transform data:\n---\n")
    transformed_lines: List[str] = []
    for line in original_content.splitlines():
        transformed_lines.append(line + "#")

    new_content: str = "\n".join(transformed_lines) + "\n"
    sys.stdout.write(new_content)
    sys.stdout.write("---\n")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    save_path: str = sys.stdin.readline().strip()

    if not save_path:
        sys.stdout.write("Not saving data.\n")
        return

    sys.stdout.write(f"Saving data to '{save_path}'\n")

    write_handle = None
    try:
        write_handle = open(save_path, 'w')
        write_handle.write(new_content)
        sys.stdout.write(f"Data saved in file '{save_path}'\n")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{save_path}': {e}\n")
        print("Data not saved.")
    finally:
        if write_handle is not None:
            write_handle.close()


if __name__ == "__main__":
    process_streams(sys.argv)

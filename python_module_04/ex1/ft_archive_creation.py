import sys
from typing import List


def process_archive(args: List[str]) -> None:
    """
    Reads an ancient text, transforms it by adding '#' to each line,
    and optionally saves it to a new file.
    """
    if len(args) != 2:
        print(f"Usage: {args[0]} <file>")
        return

    file_path: str = args[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_path}'")

    original_content: str = ""
    file_handle = None
    # Step 1: reading original file
    try:
        file_handle = open(file_path, 'r')
        print("---")
        original_content = file_handle.read()
        print(original_content,
              end="" if original_content.endswith("\n") else "\n")
        print("---")

    except Exception as e:
        print(f"Error opening file '{file_path}': {e}")
        return
    finally:
        if file_handle is not None:
            file_handle.close()
            print(f"File '{file_path}' closed.")

    # Step 2: Transformating data
    print("Transform data: ")
    print("---")
    transformed_lines: List[str] = []
    for line in original_content.splitlines():
        transformed_lines.append(line + "#")

    new_content: str = "\n".join(transformed_lines) + "\n"
    print(new_content, end="")
    print("---")

    # Step 3: saving data
    save_path: str = input("Enter new file name (or empty): ")

    if not save_path:
        print("Not saving data.")
        return

    print(f"Saving data to {save_path}")
    write_handle = None
    try:
        write_handle = open(save_path, 'w')
        write_handle.write(new_content)
        print(f"Data saved in file '{save_path}'")
    except Exception as e:
        print(f"Error saving to file '{save_path}': {e}")
    finally:
        if write_handle is not None:
            write_handle.close()


if __name__ == "__main__":
    process_archive(sys.argv)

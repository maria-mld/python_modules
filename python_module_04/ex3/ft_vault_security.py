from typing import Tuple


def secure_archive(
        filename: str,
        action: str = "read",
        content: str = ""
) -> Tuple[bool, str]:
    """
    Safely performs file operations using a context manager.
    Returns (Success, Data/Error).
    """
    try:
        if action == "read":
            with open(filename, "r") as file:
                data: str = file.read()
                return True, data
        elif action == "write":
            with open(filename, "w") as file:
                file.write(content)
                return True, "Content successfully written to file"
        return False, f"Unknown action: {action}"

    except Exception as e:
        return False, str(e)


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    result1 = secure_archive("/non/existing/file", "read")
    print(result1)

    print("Using 'secure_archive' to read from an inaccessible file:")
    result2 = secure_archive("/etc/master.passwd", "read")
    print(result2)

    print("Using 'secure_archive' to read from a regular file:")
    result3 = secure_archive("ancient_fragment.txt", "read")
    print(result3)

    if result3[0]:
        print("Using 'secure_archive' to "
              "write previous content to a new file:")
        result4 = secure_archive("vault_backup.txt", "write", result3[1])
        print(result4)


if __name__ == "__main__":
    main()

import sys


def display_command_line_args() -> None:
    print("=== Command Quest ===")

    program_name = sys.argv[0]
    print(f"Program name: {program_name}")
    arg_count = len(sys.argv) - 1

    if arg_count == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {arg_count}")

        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    display_command_line_args()

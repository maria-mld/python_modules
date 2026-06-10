import os
import site
import sys


def is_virtual_environment() -> bool:
    """
    Check if the program runs inside a virtual environment.
    """
    return sys.prefix != sys.base_prefix


def get_python_path() -> str:
    """
    Return the current Python executable path.
    """
    return sys.executable


def get_environment_name() -> str:
    """
    Return the virtual environment name.
    """
    return os.path.basename(sys.prefix)


def get_site_packages() -> str:
    """
    Return the site-packages path.
    """
    paths = site.getsitepackages()
    return paths[0]


def main() -> None:
    """
    Main program function.
    """
    inside_venv = is_virtual_environment()

    if inside_venv:
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {get_python_path()}")
        print(
            f"Virtual Environment: "
            f"{get_environment_name()}"
        )
        print(f"Environment Path: {sys.prefix}")
        print(
            "\nSUCCESS: You're in an isolated environment!"
        )
        print(
            "Safe to install packages without affecting "
            "the global system."
        )
        print(
            f"\nPackage installation path: "
            f"{get_site_packages()}"
        )
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {get_python_path()}")
        print("Virtual Environment: None detected\n")
        print(
            "WARNING: You're in the global environment!"
        )
        print(
            "The machines can see everything you install."
        )
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(
            "matrix_env\\Scripts\\activate "
            "# On Windows"
        )
        print("\nThen run this program again.")


if __name__ == "__main__":
    main()

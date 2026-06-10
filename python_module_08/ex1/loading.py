import importlib
import sys


REQUIRED_PACKAGES = [
    "pandas",
    "numpy",
    "matplotlib",
    "requests",
]


def check_dependencies() -> bool:
    """
    Check if required packages are installed.
    """
    print("LOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")

    all_installed = True

    for package in REQUIRED_PACKAGES:
        try:
            module = importlib.import_module(package)
            version = getattr(module, "__version__", "unknown")

            if package == "pandas":
                message = "Data manipulation ready"
            elif package == "numpy":
                message = "Numerical computation ready"
            elif package == "matplotlib":
                message = "Visualization ready"
            else:
                message = "Network access ready"

            print(f"[OK] {package} ({version}) - {message}")

        except ImportError:
            print(f"[MISSING] {package}")
            all_installed = False

    return all_installed


def analyze_data() -> None:
    """
    Analyze Matrix data using numpy and matplotlib.
    """
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")

    matrix_data = np.random.normal(50, 15, 1000)

    print(f"Processing {len(matrix_data)} data points...")

    dataframe = pd.DataFrame(
        {
            "signal_strength": matrix_data
        }
    )

    print("\nGenerating visualization...")

    plt.figure(figsize=(10, 5))
    plt.plot(dataframe["signal_strength"])

    plt.title("Matrix Signal Analysis")
    plt.xlabel("Time")
    plt.ylabel("Signal Strength")

    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    """
    Main function.
    """
    if not check_dependencies():
        print("\nSome dependencies are missing.\n")

        print("Install with pip:")
        print("pip install -r requirements.txt\n")

        print("Install with Poetry:")
        print("poetry install")

        sys.exit(1)

    analyze_data()


if __name__ == "__main__":
    main()

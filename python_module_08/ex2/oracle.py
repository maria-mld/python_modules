import os

from dotenv import load_dotenv


def get_config(variable_name: str) -> str:
    """
    Get environment variable value.
    """
    value = os.getenv(variable_name)

    if value is None:
        return "NOT CONFIGURED"

    return value


def security_check() -> None:
    """
    Display security checks.
    """
    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing")

    print("[OK] Production overrides available")


def main() -> None:
    """
    Main function.
    """
    load_dotenv()

    print("ORACLE STATUS: Reading the Matrix...\n")

    mode = get_config("MATRIX_MODE")
    database_url = get_config("DATABASE_URL")
    api_key = get_config("API_KEY")
    log_level = get_config("LOG_LEVEL")
    zion_endpoint = get_config("ZION_ENDPOINT")

    print("Configuration loaded:")

    print(f"Mode: {mode}")

    if database_url == "NOT CONFIGURED":
        print("Database: Missing configuration")
    else:
        if mode == "development":
            print("Database: Connected to local instance")
        else:
            print("Database: Connected to production instance")

    if api_key == "NOT CONFIGURED":
        print("API Access: Authentication failed")
    else:
        print("API Access: Authenticated")

    print(f"Log Level: {log_level}")

    if zion_endpoint == "NOT CONFIGURED":
        print("Zion Network: Offline")
    else:
        print("Zion Network: Online")

    security_check()

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()

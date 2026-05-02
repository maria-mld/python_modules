
def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature():
    print("=== Garden Temperature ===\n")
    print("Input data is '25'")
    try:
        temp = input_temperature("25")
        print(f"Temperature is now: {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")
    print("\nInput data is 'abc'")
    try:
        temp = input_temperature("abc")
        print(f"Temperature is now: {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")
    print("All temperature tests completed.")


if __name__ == "__main__":
    test_temperature()

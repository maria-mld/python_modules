import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            line = input("Enter new coordinates as floats in format 'x,y,z': ")
            parts = line.split(",")

            if len(parts) != 3:
                print("Invalid syntax")
                continue

            x = float(parts[0].strip())
            y = float(parts[1].strip())
            z = float(parts[2].strip())

            return (x, y, z)

        except ValueError as e:
            err_msg = str(e).split(":")[-1].strip()
            print(f"Error on parameter: could not "
                  f"convert string to float: {err_msg}")


def run_tracker() -> None:
    print("=== Game Coordinate. System ===")
    print("Get a first set of coordinates")

    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    x1, y1, z1 = pos1
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")

    dist_to_center = math.sqrt(x1**2 + y1**2 + z1**2)
    print(f"Distance to center: {round(dist_to_center, 4)}")

    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    x2, y2, z2 = pos2

    dist_between = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between the 2 sets of "
          f"coordinates: {round(dist_between, 4)}")


if __name__ == "__main__":
    run_tracker()

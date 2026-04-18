# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_custom_errors.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: maria <maria@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/12 18:05:33 by maria             #+#    #+#              #
#    Updated: 2026/04/12 18:34:00 by maria            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)
        
class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)

def check_plant() -> None:
    raise PlantError("The tomato plant is wilting!")

def check_water() -> None:
    raise WaterError("Not enough water in the tank!")

def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("\nTesting PlantError...")
    try:
        check_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        
    print("\nTesting WaterError...")
    try:
        check_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        check_plant()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        
    print("\nAll custom error types work correctly!")

if __name__ == "__main__":
    test_custom_errors()
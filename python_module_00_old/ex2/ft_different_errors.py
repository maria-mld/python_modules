# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_different_errors.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: maria <maria@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/12 17:44:53 by maria             #+#    #+#              #
#    Updated: 2026/04/12 18:03:35 by maria            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def garden_operations(operation_number : int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        x = 1 / 0
    elif operation_number == 2:
        open("file.txt")
    elif operation_number == 3:
        result = "hello" + 5
    else:
        print("operations completed successfully")

def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        print(f"Testing operation {i}. . .")
        try:
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print("\nAll error types tested successfully!")

if __name__ == "__main__":
    test_error_types()
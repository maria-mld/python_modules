# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_first_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: maria <maria@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/11 13:08:14 by maria             #+#    #+#              #
#    Updated: 2026/04/18 15:16:18 by maria            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def input_temperature(tenp_str : str) -> int:
    return int(tenp_str)

def test_temperature():
    print("=== Garden Temperature ===\n")
    print(f"Input data is '25'")
    try:
        temp = input_temperature("25")
        print(f"Temperature is now: {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")
    print(f"\nInput data is 'abc'")
    try:
        temp = input_temperature("abc")
        print(f"Temperature is now: {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")
    print("All temperature tests completed.")
    
    
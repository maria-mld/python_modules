def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count(day, max_days):
        if day > max_days:
            print("Harvest time!")
            return
        print(f"Day {day}")
        count(day + 1, max_days)
    count(1, days)

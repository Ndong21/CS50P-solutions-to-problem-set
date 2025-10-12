def main() -> None:
    time: float = convert(input("What time is it? "))

    # breakfast time
    breakfast_start: int = 7
    breakfast_end: int = 8

    # lunch time
    lunch_start: int = 12
    lunch_end: int = 13

    # dinner time
    dinner_start: int = 18
    dinner_end: int = 19

    if breakfast_start <= time <= breakfast_end:
        print("breakfast time")
    elif lunch_start <= time <= lunch_end:
        print("lunch time")
    elif dinner_start <= time <= dinner_end:
        print("dinner time")


def convert(time: str) -> float:
    hour, minutes = time.split(":")

    hour_num: float = float(hour)
    minutes_to_hour_num: float = round(float(minutes) / 60, 1)

    return hour_num + minutes_to_hour_num


if __name__ == "__main__":
    main()

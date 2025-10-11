def main() -> None:
    dollars: float = dollars_to_float(input("How much was the meal? "))

    percent: float = percent_to_float(input("What percentage would you like to tip? "))

    tip: float = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    converted_dollars: float = float(d.replace("$", ""))

    return converted_dollars


def percent_to_float(p: str) -> float:
    converted_percent: float = float(p.replace("%", "")) / 100

    return converted_percent


main()

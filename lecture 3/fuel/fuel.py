while True:
    fraction: str = input("Fraction: ")
    try:
        numerator, denominator = fraction.split("/")

        x = int(numerator)
        y = int(denominator)

    except (ValueError, ZeroDivisionError):
        pass

    else:
        if x <= y:
            fuel_left: float = x / y * 100
            fuel_percentage: int = int(f"{fuel_left:.0f}")

            if fuel_percentage <= 1:
                print("E")
                break
            elif fuel_percentage >= 99:  # noqa: PLR2004
                print("F")
                break
            else:
                print(f"{fuel_percentage}%")
                break

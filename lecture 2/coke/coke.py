def main() -> None:
    change: int = make_payment()
    print(f"Change Owed: {change}")


def make_payment() -> int:
    cost: int = 50
    change: int = -50
    while True:
        print(f"Amount Due: {cost}")
        coin: int = int(input("Insert coin: "))
        accepted_denominations: list[int] = [25, 10, 5]

        if coin in accepted_denominations:
            cost -= coin
            change += coin

            if change >= 0:
                return change


main()

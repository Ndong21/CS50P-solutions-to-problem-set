def main() -> None:
    greet()


def greet() -> None:
    greeting: str = input("Enter your greetings here: ").lower()

    if greeting.startswith("hello"):
        print("0$")
    elif greeting.startswith("h") and greeting != "hello":
        print("$20")
    else:
        print("$100")


main()

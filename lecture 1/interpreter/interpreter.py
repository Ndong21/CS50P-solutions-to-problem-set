def main() -> None:
    interpreter()


def interpreter() -> None:
    expression: str = input("Enter expression: ")

    x, y, z = expression.split(" ")

    match y:
        case "+":
            print(float(x) + float(z))
        case "-":
            print(float(x) - float(z))
        case "*":
            print(float(x) * float(z))
        case "/":
            print(float(x) / float(z))
        case _:
            print("No math operation specified")


main()

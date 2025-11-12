def main() -> None:
    convert_to_snake_case(input("Enter variable name (in camelCase): "))


def convert_to_snake_case(name: str) -> None:
    for character in name:
        if character.islower():
            print(character, end="")
        else:
            print(f"_{character.lower()}", end="")
    print()


main()

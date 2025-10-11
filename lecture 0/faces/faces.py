def main() -> None:
    print(convert())


def convert() -> str:
    text: str = input("Enter your text ")

    if ":)" in text:
        text = text.replace(":)", "🙂")

    if ":(" in text:
        text = text.replace(":(", "🙁")

    return text

    # another solution below, which then is more efficient. above or below
    # return text.replace(":)", "🙂").replace(":(", "🙁")


main()

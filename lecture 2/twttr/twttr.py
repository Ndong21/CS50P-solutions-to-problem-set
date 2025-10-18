def text_shortener() -> None:
    text: str = input("Input: ")

    vowels: list[str] = ["a", "e", "i", "o", "u"]

    for character in text:
        if character.lower() in vowels:
            text = text.replace(character, "")

    print(f"Output: {text}")


text_shortener()

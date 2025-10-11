def playback() -> str:
    text: str = input("Enter any sentence or text ")

    return text.replace(" ", "...")


print(playback())

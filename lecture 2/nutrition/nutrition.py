def fruit_calories() -> None:
    calories_info: list[dict[str, int]] = [
        {"Apple": 130},
        {"Avocado": 50},
        {"Banana": 110},
        {"Cantaloupe": 50},
        {"Grapefruit": 60},
        {"Grapes": 90},
        {"Honeydew": 50},
        {"Kiwifruit": 90},
        {"Lemon": 15},
        {"Sweet Cherries": 100},
    ]

    item: str = input("Item: ").title()

    for fruit in calories_info:
        if item in fruit:
            print(f"Calories: {fruit[item]}")


fruit_calories()

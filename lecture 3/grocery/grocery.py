lists: dict[str, int] = {}
while True:
    try:
        item: str = input().upper()

    except EOFError:
        print()
        break

    else:
        if item in lists:
            lists[item] += 1

        else:
            lists[item] = 1

for key, value in sorted(lists.items()):
    print(value, key)

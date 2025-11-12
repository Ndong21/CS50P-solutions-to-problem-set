month_list: list[str] = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    date = input("Date: ")

    if date.rfind("/") >= 0:
        try:
            m, d, y = date.split("/")
            month_num: int = int(m)
            day: int = int(d)
            year: int = int(y)

            if (month_num <= 12) & (day <= 31):  # noqa: PLR2004
                break

        except Exception:  # noqa: BLE001, S110
            pass
    else:
        try:
            m, d, y = date.split(" ")
            d = d.split(",")[0]

            m = m.title()
            day: int = int(d)
            year: int = int(y)
            month_num: int = 0

            if (m.title() in month_list) & (day <= 31):  # noqa: PLR2004
                month_num = month_list.index(m) + 1
                break

        except Exception:  # noqa: BLE001, S110
            pass

print(f"{year}-{month_num:02}-{day:02}")  # type: ignore  # noqa: PGH003

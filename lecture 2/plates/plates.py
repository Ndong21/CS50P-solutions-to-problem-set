def main() -> None:
    plate: str = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool:
    return (
        plate_start_with_two_letters(s)
        and length_of_plate_is_ok(s)
        and numbers_in_correct_position(s)
        and plate_do_not_contain_puntuation(s)
    )


def plate_start_with_two_letters(s: str) -> bool:
    first_two: str = s[:2]

    return first_two.isalpha()


def length_of_plate_is_ok(s: str) -> bool:
    min_characters: int = 2
    max_characters: int = 6
    return min_characters <= len(s) <= max_characters


def numbers_in_correct_position(s: str) -> bool:
    seen_number: bool = False
    first_number_found: bool = False

    for ch in s:
        if ch.isdigit():
            if not seen_number:
                seen_number = True
                first_number_found = True
                # check if the first number is 0
                if ch == "0" and first_number_found:
                    return False
        elif seen_number:
            # if a letter appears after numbers started -> invalid
            return False

    return True


def plate_do_not_contain_puntuation(s: str) -> bool:
    for ch in s:
        if ch.isalnum():
            pass
        else:
            return False

    return True


main()

def energy() -> int:
    mass: int = int(input("Enter the mass in Kg "))
    speed: int = 300000000

    return mass * speed**2


print(energy())

# question 1
print("The Great Question of Life, the Universe and Everything ")
answer: str = input("Enter the answer to the question above: ").lower()

if answer == "42" or ("forty" in answer and "two" in answer):
    print("Yes")
else:
    print("No")

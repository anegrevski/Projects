import random

number = random.randint(1,100)

while True:
    num_get = input("Guess the number (1-100): ")
    if not num_get.isdigit():
        print("Invalid input. Try again...")
        continue
    num_get1 = int(num_get)
    if num_get1 == number:
        print("You guess!")
        break
    elif num_get1 < number:
        print("Too low")

    else:
        print("Too high")

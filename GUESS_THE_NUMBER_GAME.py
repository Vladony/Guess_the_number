import random


def easy():
    same_digits = 0
    same_positions = 0
    number_of_guess = int(input("Tell us how many tries you would like to have: "))
    tries = 0

    number_to_find = random.sample(range(1, 9), 4)

    while True:
        tries += 1
        same_positions = 0
        same_digits = 0

        if tries > number_of_guess:
            number_to_find = "".join(map(str, number_to_find))
            print(f'Sorry, you have no more tries left. The number was : {number_to_find}')
            exit()
        guess = int(input("Give us your guess: "))
        guess = list(str(guess))
        guess = [int(d) for d in guess]

        for i in number_to_find:
            for j in guess:
                if i == j:
                    same_digits += 1
        print(f"You have {same_digits} same digits.")

        for m in range(len(number_to_find)):
            for n in range(len(guess)):
                if number_to_find[m] == guess[n] and m == n:
                    same_positions += 1
        print(f"You have {same_positions} correct positions.")

        if same_positions == 4:
            number_to_find = "".join(map(str, number_to_find))
            print(f'YOU WON! The number was: {number_to_find} and you did it on your {tries} try.')
            exit()


def medium():
    same_digits = 0
    same_positions = 0
    number_of_guess = int(input("Tell us how many tries you would like to have: "))
    tries = 0

    while True:
        number_to_find = random.sample(range(0, 9), 4)
        if number_to_find[0] == 0:
            continue
        else:
            break

    while True:
        tries += 1
        same_positions = 0
        same_digits = 0

        if tries > number_of_guess:
            number_to_find = "".join(map(str, number_to_find))
            print(f'Sorry, you have no more tries left. The number was : {number_to_find}')
            exit()
        guess = int(input("Give us your guess: "))
        guess = list(str(guess))
        guess = [int(d) for d in guess]

        for i in number_to_find:
            for j in guess:
                if i == j:
                    same_digits += 1
        print(f"You have {same_digits} same digits.")

        for m in range(len(number_to_find)):
            for n in range(len(guess)):
                if number_to_find[m] == guess[n] and m == n:
                    same_positions += 1
        print(f"You have {same_positions} correct positions.")

        if same_positions == 4:
            number_to_find = "".join(map(str, number_to_find))
            print(f'YOU WON! The number was: {number_to_find} and you did it on your {tries} try.')
            exit()


def hard():
    same_digits = 0
    same_positions = 0
    number_of_guess = int(input("Tell us how many tries you would like to have: "))
    number_of_digits = int(input("Tell us how many digits would you like the number to be: "))
    tries = 0

    while True:
        number_to_find = random.sample(range(0, 9), number_of_digits)
        if number_to_find[0] == 0:
            continue
        else:
            break

    while True:
        tries += 1
        same_positions = 0
        same_digits = 0

        if tries > number_of_guess:
            number_to_find = "".join(map(str, number_to_find))
            print(f'Sorry, you have no more tries left. The number was : {number_to_find}')
            exit()
        guess = int(input("Give us your guess: "))
        guess = list(str(guess))
        guess = [int(d) for d in guess]
        if len(guess) < number_of_digits:
            print(f"You need to enter a {number_of_digits} digit number!")
            continue

        for i in number_to_find:
            for j in guess:
                if i == j:
                    same_digits += 1
        print(f"You have {same_digits} same digits.")

        for m in range(len(number_to_find)):
            for n in range(len(guess)):
                if number_to_find[m] == guess[n] and m == n:
                    same_positions += 1
        print(f"You have {same_positions} correct positions.")

        if same_positions == 4:
            number_to_find = "".join(map(str, number_to_find))
            print(f'YOU WON! The number was: {number_to_find} and you did it on your {tries} try.')
            exit()


difficulty = input("Hello and welcome to the 'Guess the number'."
                   "Please select your difficulty(Easy, Medium or Hard): ")
bool_diff = False

while not bool_diff:
    if difficulty.lower() == "easy":
        bool_diff = True
        easy()
    elif difficulty.lower() == "medium":
        bool_diff = True
        medium()
    elif difficulty.lower() == "hard":
        bool_diff = True
        hard()
    else:
        difficulty = input("Please enter a valid difficulty:")

__author__: str = "730643371"


def guess_a_number() -> None:
    secret: int = 7
    num: int = int(input("Guess a number:"))
    print("Your guess was " + str(num))
    if num == secret:
        print("You got it!")
    elif num < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()

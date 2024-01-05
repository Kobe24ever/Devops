import random

difficulty = int(input("What is the difficulty level? "))
secret_number = random.randint(1, difficulty + 1)
get_guess_from_user = int(input("Guess a number: "))
compare_results = secret_number == get_guess_from_user
print(f"\nNumber generated: {secret_number}")
print(f"User guess: {get_guess_from_user}")


def play(compare_results):
    if compare_results:
        return "You Won!!!"
    else:
        return "You Lost!!!"


result = play(compare_results)
print(f"Result of game: {result}")
import random
import prompt


def prime_game():
    correct_answers = 0
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while correct_answers < 3:
        random_number = random.randrange(0, 10, 1)
        print(f'Question: {random_number}')
        answer_gamer = prompt.string('Your answer: ')
        if is_prime(random_number) == answer_gamer:
            print("Correct!")
            correct_answers += 1
            continue
        else:
            print(f"'{answer_gamer}' is wrong answer ;(. "
                  f"Correct answer was '{is_prime(random_number)}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


def is_prime(number):
    if number == 0 or number == 1:
        return "no"
    else:
        for i in range(2, number):
            if number % i == 0:
                return "no"
        return "yes"

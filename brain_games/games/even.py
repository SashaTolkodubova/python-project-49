import prompt
import random


def even_game():
    correct_answers = 0
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while correct_answers < 3:
        random_number = random.randrange(1, 99, 1)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0:
            if answer == 'yes':
                print("Correct!")
                correct_answers += 1
                continue
            else:
                print(f"'{answer}' is wrong answer ;(. "
                      f"Correct answer was 'no'.")

                print(f"Let's try again, {name}!")
                return

        else:
            if answer == 'no':
                print("Correct!")
                correct_answers += 1
                continue
            else:
                print(f"'{answer}' is wrong answer ;(. "
                      f"Correct answer was 'yes'.")

                print(f"Let's try again, {name}!")
                return
    print(f"Congratulations, {name}!")

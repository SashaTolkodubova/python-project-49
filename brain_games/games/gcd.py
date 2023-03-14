import random
import prompt


def gcd_game():
    correct_answers = 0
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    while correct_answers < 3:
        random_number_1 = random.randrange(1, 99, 1)
        random_number_2 = random.randrange(1, 99, 1)
        print(f'Question: {random_number_1} {random_number_2}')
        answer_gamer = prompt.string('Your answer: ')
        correct_answer = gcd(random_number_1, random_number_2)

        if answer_gamer == str(correct_answer):
            print("Correct!")
            correct_answers += 1
            continue
        else:
            print(f"'{answer_gamer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")

            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


def gcd(number1, number2):
    if number1 == number2:
        return number1
    elif number1 > number2:
        while number1 % number2 != 0:
            temp = number2
            number2 = number1 % number2
            number1 = temp
        return number2
    else:
        while number2 % number1 != 0:
            temp = number1
            number1 = number2 % number1
            number2 = temp
        return number1

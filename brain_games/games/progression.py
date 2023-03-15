import random
import prompt


def progression():
    correct_answers = 0
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    while correct_answers < 3:
        start_random_number = random.randrange(1, 50, 1)
        random_step = random.randrange(1, 10, 1)
        random_number_in_array = random.randrange(0, 9, 1)
        result_array = [str(start_random_number)]

        for i in range(9):
            start_random_number += random_step
            result_array.append(str(start_random_number))

        correct_answer = result_array[random_number_in_array]
        result_array[random_number_in_array] = '..'
        print(f'Question: {" ".join(result_array)}')
        answer_gamer = prompt.string('Your answer: ')
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

import operator
import random
import prompt

def calc():
    correct_answers = 0
    random_number_operator = random.randrange(1,3, 1)
    random_number_1 = random.randrange(1,99, 1)
    random_number_2 = random.randrange(1,99, 1)
    operators  = {
        1 : operator.sub,
        2 : operator.add,
        3 : operator.mul
    }

    string_operators = {
        1 : "-",
        2 : "+",
        3 : "* " 
    }

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    while correct_answers < 3:
        random_number_operator = random.randrange(1,3, 1)
        random_number_1 = random.randrange(1,99, 1)
        random_number_2 = random.randrange(1,99, 1)
        print(f'Question: {random_number_1} {string_operators[random_number_operator]} {random_number_2}')
        answer_gamer = prompt.string('Your answer: ')
        correct_answer = operators[random_number_operator](random_number_1, random_number_2)
        if answer_gamer == str(correct_answer):
                print("Correct!")
                correct_answers += 1
                continue
        else:
                print(f"'{answer_gamer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
                print(f"Let's try again, {name}!")
                return
    print(f"Congratulations, {name}!")
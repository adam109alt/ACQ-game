# ACQ
from The_data_CLI import quiz_dataset
import random

name = input("What is your name: ").capitalize()
print(f"Welcome {name}❤️")

print("And welcome to our, Question game, press(q), to quit")

while True:
    age = input("Enter your age: ")

    if age.isdigit():
        age = int(age)

        if age > 100:
            print("Sorry, you are too old to play")
            exit()

        elif age < 5:
            print("Sorry you are too small for this")
            exit()

        else:
            break
    else:
        print("Invalid.")
        continue

while True:
    play = input("Do you want to play? ").lower()

    if play == "yes":
        print(f"Welcome to our game {name}\n")
        break

    elif play == "no":
        print("see you ❤️")
        exit()

    else:
        print("Invalid, please enter (yes or no)\n")


def main():
    # points variable
    points = 0
    # ask the question
    while True:
        
        topic = random.choice(quiz_dataset)
    
        print(f"{topic['question']}")
        print(f"Choices: {str(topic['choices']).strip('[]').replace("'", '')} ")
        answer = input("Enter your answer: ")
        
        answer = answer.title()

        if answer == topic["correct_answer"]:
            if topic["difficulty"] == "easy":
                points += 10
                print(f"Right! you answerd an easy question, Your points now is: {points}")
                print(f"The Explanition {topic['explanation']}\n")
                cont = input(f"Do you want to continue (q to quit, enter to continue)? ")
                if cont == "q":
                    print(f"See you {name}, your score is: {points}")
                    exit()
                else:
                    continue

            elif topic["difficulty"] == "medium":
                points += 20
                print(
                    f"Right! you answerd an medium question, Your points now is: {points}"
                )
                print(f"The Explanition {topic['explanation']}\n")
                cont = input(
                    f"Do you want to continue (q to quit, enter to continue)? "
                )
                if cont == "q":
                    print(f"See you {name}, your score is: {points}")
                    exit()
                else:
                    continue

            elif topic["difficulty"] == "hard":
                points += 30
                print(
                    f"Right! you answerd an hard question, Your points now is: {points}"
                )
                print(f"The Explanition {topic['explanation']}\n")
                cont = input(
                    f"Do you want to continue (q to quit, enter to continue)? "
                )
                if cont == "q":
                    print(f"See you {name}, your score is: {points}")
                    exit()
                else:
                    continue

        else:
            print(f"Sorry Wrong answer the true answer is: {topic['correct_answer']}\n")
            print(f"The Explanition {topic['explanation']}\n")
            cont = input(f"Do you want to continue (q to quit, enter to continue)? ")
            if cont == "q":
                print(f"See you {name}, your score is: {points}")
                exit()
            else:
                continue


main()


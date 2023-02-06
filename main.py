import csv
import random
import subprocess

print('Welcome to my quiz')
print('GOOD LUCK!')
print('')

def read_questions():
    with open('questions.csv', 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)

questions = read_questions()
score = 0
for question in questions:
    options = [question['Option1'], question['Option2'], question['Option3'], question['Option4']]
    random.shuffle(options)
 #   subprocess.call("clear", shell=True)
    print(question['Question'])
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    answer = int(input("Enter the number of your answer: "))
    if options[answer-1] == question['Option1']:
        subprocess.call("clear", shell=True)
        print("Correct!")
        score += 1
    else:
        subprocess.call("clear", shell=True)
        print("Incorrect.")

print(f"You got {score} out of {len(questions)} questions correct.")

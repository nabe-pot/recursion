import random

print("This is a number guessing game.You will be asked to two numbers.")
print("I will generate a random number between the two numbers.You will try to guess the number.")
n = int(input("Enter a first number: "))
m = int(input("Enter a greater number than the first: "))
number_of_attempts = int(input("Enter the number of attempts: "))

while n > m:
    print("================================================================================")
    print("The second number is lower than the first number. Prease enter a greater number.")
    n = input("Enter a number: ")
    m = input("Enter a greater number than the first: ")

random_number = random.randint(n, m)

print("==================================================================")
print("I have a number between", n, "and", m, ". Can you guess my number?")
user_guess = int(input("Enter your guess: "))

for _ in range(number_of_attempts - 1):
    if user_guess != random_number:
        print("====================================")
        print("Wrong! Try again.")
        user_guess = int(input("Enter your guess: "))
    else:
        print("=============================================")
        print("Congratulations! You have guessed the number.")
        break

print("You Lose")


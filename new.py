# Databricks notebook source
print("hello world")

# COMMAND ----------

number1 = 22
number2 = 23

print("sum: ", number1 + number2)
print("subtraction: ", number1 - number2)
print("multiplication: ", number1 * number2)
print("division: ", number1 / number2)

print("Integer Division: ", number1 // number2)
print("Modulo: ", number1 % number2)

# COMMAND ----------

number1 = input("enter a number plz")
number2 = input("do it again u scrub")

print(int(number1), int(number2), int(number1) + int(number2))

# COMMAND ----------

var_1 = 12

var_2 = 13

print(var_1 == var_2)
print(var_1 < var_2)
print(var_1 > var_2)
print(var_1 != var_2) #not equal to 
print(var_1 <= var_2)
print(var_1 >= var_2)

# COMMAND ----------

num1 = 18
num2 = 12

if num1 < num2:
    print("num2 is greater")
elif num1 == num2:
    print("theyre equal mate")

else:
    print("num1 is greater")

# COMMAND ----------

number1 = input("enter a number plz")
number2 = input("do it again u scrub")

if number1 > number2:
    print("number1 is greater")
elif number1 < number2:
    print("number 2 is greater")
elif number1 == number2:
    print("they're equal bro")

# COMMAND ----------

number1 = input("what year were you born")

if(int(number1) % 4 == 0):
    print("you're born on a leap year")
    
else:
    print("you're not born on a leap year")







# COMMAND ----------

products = [1,2,3,4,5,6,7,8,9,11,12]

for counter in range(2,3):
    print(counter)

# COMMAND ----------

products = [1,2,3,4,5,6,7,8,9,11,12]

for counter in range(len(products)):
    print(counter, products[counter])

# COMMAND ----------

num = 2.71828182845

print(round(num, 3))

# COMMAND ----------

def hello():
    print("hello world")
    
def goodbye():
    print("goodbye world")

hello()
goodbye()


# COMMAND ----------


def convert(number):
    conversion = number / 2.2
    return conversion

num_to_convert = 100

answer = convert(num_to_convert)

print("the kilo equivalent of " + str(num_to_convert) + "lbs is", answer, "kgs")

# COMMAND ----------


def convert(number):
    conversion = number / 2.2
    return conversion

num_to_convert = 20

answer = convert(num_to_convert)

print("the kilo equivalent of " + str(num_to_convert) + " lbs is" ,answer, "kgs")

# COMMAND ----------


def convert(number):
    conversion = (number - 32) *5/9 
    return conversion

num_to_convert = 32

answer = convert(num_to_convert)

print("the celcius equivalent of " + str(num_to_convert) + " degrees is", answer, "degrees")

# COMMAND ----------


def convert(number):
    conversion = (number - 32) *5/9 
    return conversion

num_to_convert = 100

answer = convert(num_to_convert)

print("the celcius equivalent of " + str(num_to_convert) + " degrees is", answer, "degrees")

# COMMAND ----------

my_list = ["i", "d", "l", "e"]

#del my_list[2:4] - refers to cells starting at 0, so will only delete l and e as they are in the range of 2-4
#my_list[1] = "n"
new_list = ["s"] + my_list
new_list.append("g")

print(new_list)

# COMMAND ----------

import random

my_list = ["i", "d", "l", "e"]

#del my_list[2:4] - refers to cells starting at 0, so will only delete l and e as they are in the range of 2-4
#my_list[1] = "n"
#new_list = ["s"] + my_list
#new_list.append("g")


final_list = []
for i in my_list:
    print(i, my_list.index(i))
    final_list.append(my_list.index(i))

print(final_list)

print(sum(final_list))
print(len(final_list))

# COMMAND ----------


integer_list = [0,1,2,3,4,5,6,7,8,9,11]

average_integers = sum(integer_list) / len(integer_list)

print(sum(integer_list))
print(len(integer_list))
print(average_integers)

final_lists = []
for i in integer_list:
    print(i, integer_list.index(i))
    final_lists.append(integer_list.index(i))
    if i == average_integers:
        print("The number is equal to the average")
    elif i < average_integers:
        print("The number is less than average")
    elif i > average_integers:
        print("The number is greater than average")
    


# COMMAND ----------

addition(3,2)

# COMMAND ----------

num1 = input("input a number")
num2 = input("Input another")

total = float(num1) + float(num2)

print(total)


# COMMAND ----------

def fifty_thirty_twenty(ati):
    return {
        "needs" : 0.5*ati, 
        "wants" : 0.3*ati,
        "savings" : 0.2*ati,
    }

    ati = 100
    
print(fifty_thirty_twenty)      

# COMMAND ----------

import random

list_numbers = [1,2,3,4,5,6]

while True:
    guess = input("roll the dice")
    if(list_numbers) == 0:
        break
    else:
        chosen_number = random.choice(list_numbers)
        print(chosen_number)
        
print("roll again? ")






# COMMAND ----------

# DBTITLE 1,Dice roll, got this online, not my code. https://realpython.com/python-dice-roll/
def parse_input(input_string):
    """Return `input_string` as an integer between 1 and 6.

    Check if `input_string` is an integer number between 1 and 6.
    If so, return an integer with the same value. Otherwise, tell
    the user to enter a valid number and quit the program.
    """
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)

import random


def roll_dice(num_dice):
    roll_results = []
    for i in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results

num_dice_input = input("How many dice do you want to roll? [1-6] ")
num_dice = parse_input(num_dice_input)
# 2. Roll the dice
roll_results = roll_dice(num_dice)

print(roll_results)


# COMMAND ----------


import random

number_to_guess = random.randint

def number_to_guess(choice_int):
    if int(choice_int) > int(number_to_guess):
        return ("Your choice is larger than what I'm thinking of, guess again")
    elif int(choice_int) < int(number_to_guess):
        return ("Your choice is smaller than what I'm thinking of, guess again")
    elif int(choice_int) == int(number_to_guess):
        return ("Thats the number I'm thinking of")
    

user_choice = input("What number am I thinking of?")

print(number_to_guess)



# COMMAND ----------

# DBTITLE 1,Number guess, got this online, not my code. https://thecleverprogrammer.com/2022/06/29/number-guessing-game-using-python/
import random
n = random.randrange(1,10)
guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
          break
print("you guessed it right!!")

# COMMAND ----------

# DBTITLE 1,Mad libs
noun = input(str("Give me a singular noun"))
verb = input(str("Give me a verb"))
adjective = input(str("Give me an adjective"))
emotion = input(str("Give me an emotion"))

print("i dont know if this will " + noun)
print("it is " + verb)
print("i am " + adjective)
print("i feel " + emotion)



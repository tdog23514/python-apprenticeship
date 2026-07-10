------------------------------------------------------------------------
Module 01 - Lesson 05
Topic: Conditional Statements (if, elif, else)
Author: Timothy White
Date: 2026-07-09
------------------------------------------------------------------------

age = int(input("Enter your age: "))
if age >= 18: 
    print("You are an adult.")
else: 
    print("You are a minor.")

score = float(input("Enter test score: "))
if score >= 70:
    print("You passed! Great job!")
elif score >= 90:
    print("You got an A! Excellent work!")
else:
    print("You failed.")

temp = int(input("Enter the temperature in Fahrenheit: "))
if temp >= 85:
    print("It's hot outside today!")
elif temp >= 60:
    print("It's very cozy outside today!")
else:
    print("It's cold outside today!")
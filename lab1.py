#!/usr/bin/env python3

try:
	birth_year = int(input("Enter your birth year: "))
	current_year = 2024 
	age = current_year - birth_year
	
	print("Your age is:", + age)

except ValueError:
	print("Please enter an int")

def helloWorld():
	print('Hello World')
helloWorld()

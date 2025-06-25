#!/usr/bin/env python3
age_input = input("Please tell me your age: ")
age = int(age_input)

print("You are currently", age, "years old.")

for years in [10, 20, 30]:
    print("In", years, "years, you'll be", age + years, "years old.")

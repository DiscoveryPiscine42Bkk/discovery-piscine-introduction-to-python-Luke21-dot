#!/usr/bin/env python3
prompt = "What you gotta say? : "
while True:
    user_input = input(prompt)
    if user_input == "STOP":
        break
    prompt = "I got that! Anything else? : "

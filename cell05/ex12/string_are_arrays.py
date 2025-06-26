#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    input_str = sys.argv[1]
    result = ''
    for char in input_str:
        if char == 'z':


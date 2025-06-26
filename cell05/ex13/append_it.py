#!/usr/bin/env python3

import sys
import re

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    for word in args:
        if re.search(r'ism$', word):
            continue
        print(f"{word}ism")

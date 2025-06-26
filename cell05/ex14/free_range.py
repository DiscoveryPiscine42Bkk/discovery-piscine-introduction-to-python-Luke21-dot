#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("none")
else:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        nums = list(range(start, end + 1)) if start <= end else list(range(start, end - 1, -1))

        print(nums)
    except ValueError:
        print("none")

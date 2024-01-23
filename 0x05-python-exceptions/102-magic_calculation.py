#!/usr/bin/python3
def magic_calculation(a, b):
    ans = 0
    for index in range(1, 3):
        try:
            if index > a:
                raise Exception("Too far")
            else:
                ans += (a ** b) / index
        except Exception:
            ans = b + a
            break
    return ans

import sys

def fib(n):
    a, b = 0, 1
    while a < n:
        print a,         # The comma stops a newline
        a, b = b, a+b

try:
    val = int(sys.argv[1])
except ValueError:
    val = 2000

fib(val)

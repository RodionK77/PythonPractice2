import sys


def my_print(*pr, sep=' ', end='\n'):
    sys.stdout.write(sep.join([str(x) for x in pr]) + end)


my_print('hello', 100, "two 2")

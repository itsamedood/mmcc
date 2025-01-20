from sys import exit


def throw(code = 1, *args: str): [print(a) for a in args]; exit(code)

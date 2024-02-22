

def escribe_raro(n):
    if n > 0:
        print(n, end="")
        escribe_raro(n - 1)
        print(n, end="")
    else:
        print(0, end="")


escribe_raro(5)
from typing import Iterator

from SEMINARIOS.Seminario1.Ej2 import take


def es_primo(k):
    for n in range(2, k):
        if k % n == 0:
            return False
    return True

def primos() -> Iterator[int]:
    p = 2
    while True:
        if es_primo(p):
            yield p
        p += 1


def squares1():
    num=1
    while True:
        yield (num*num)+1
        num+=1

def almost_squares():
    s=squares1()
    p=primos()

    sq=next(s)
    pr=next(p)
    while True:
        if sq==pr :
            yield pr
            pr=next(p)
            sq=next(s)
        elif pr<sq:
            pr=next(p)
        else:
            sq=next(s)



if __name__ == "__main__":
    n = 10
    iter=almost_squares()
    print(list(take(10, almost_squares())))



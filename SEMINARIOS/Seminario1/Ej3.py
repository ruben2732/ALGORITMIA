from typing import Iterator

from SEMINARIOS.Seminario1.Ej2 import take


def squares1():
    num=1
    while True:
        yield (num*num)+1
        num+=1

if __name__ == "__main__":
    n = 10
    iter=squares1()
    print(list(take(10, squares1())))




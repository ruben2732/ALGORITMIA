#!/usr/bin/env python3
import sys
from typing import Iterator



def read_data(f):
    read=f.readline()
    return int(read)

def take(n: int, it: Iterator[int]):
    num=0
    while num<n:
        yield next(it)
        num+=1

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

def show_results(results):
    it=results
    for i in it:
        print(i)


def process(n: int):
    return take(n, almost_squares())


if __name__ == "__main__":
    n = read_data(sys.stdin)
    l = process(n)
    show_results(l)
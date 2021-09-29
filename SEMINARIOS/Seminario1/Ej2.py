from typing import Iterator

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

def take(n: int, it: Iterator[int]):
    num=0
    while num<n:
        yield next(it)
        num+=1

if __name__ == "__main__":
    n = 10
    todos = primos()
    print(list(take(10, primos())))



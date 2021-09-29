#!/usr/bin/env python3
import sys

def read_data(f):
    # Leer del fichero f
    lines = f.readlines()
    # Transformamos cada línea en un entero:
    return [int(line) for line in lines]

def show_results(nums):
    # Escribir los resultados
    print("No hay repetidos" if not results else "Hay repetidos")

def process(nums):
    sums = set()
    for num in nums:
        for s in list(sums):
            sums.add(s+num)
        sums.add(num)
    return len(sums)

if __name__ == "__main__":
    nums = read_data(sys.stdin)
    results = process(nums)
    show_results(results)
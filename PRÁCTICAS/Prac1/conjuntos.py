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

def process(data):
    seen = set()
    for n in data:
        if n in seen:
            return True
        seen.add(n)
    return False

if __name__ == "__main__":
    nums = read_data(sys.stdin)
    results = process(nums)
    show_results(results)
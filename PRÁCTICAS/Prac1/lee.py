#!/usr/bin/env python3
import sys
def read_data(f):
    # Leer del fichero f
    lines = f.readlines()
    # Transformamos cada línea en un entero:
    return [int(line) for line in lines]
def show_results(nums):
    # Escribir los resultados
    for num in nums:
        print(num)
if __name__ == "__main__":
    nums = read_data(sys.stdin)
    show_results(nums)
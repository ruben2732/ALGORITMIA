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

def process_1(data):
    repeated = False
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] == data[j]:
                repeated = True
    return repeated

def process_2(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] == data[j]:
                return True
    return False

def process_3(data):
    data.sort()
    for i in range(0, len(data)-1):
        if data[i] == data[i+1]:
            return True
    return False

if __name__ == "__main__":
    nums = read_data(sys.stdin)
    results = process_3(nums)
    show_results(results)

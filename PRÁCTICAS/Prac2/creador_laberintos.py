from typing import *
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from random import shuffle
import sys

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]

def read_data(f: TextIO):
    rows = int(f.readline())
    cols = int(f.readline())
    return rows, cols

def process(rows: int, cols: int) -> UndirectedGraph:
    #Paso 1:
    vertices = [(r,c) for r in range(rows) for c in range (cols)]

    #Paso 2:
    mfs = MergeFindSet()
    for v in vertices: mfs.add(v)

    #Paso 3:
    edges = []
    for r in range(rows):
        for c in range(cols):
            if r < rows - 1: edges.append(((r,c), (r + 1,c)))
            if c < cols - 1: edges.append(((r, c), (r, c  + 1)))
    shuffle(edges)

    #Paso 4:
    corridors = []

    #Paso 5:
    for (u , v) in edges:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u ,v)
            corridors.append((u,v))
    #Paso 6:
    return UndirectedGraph(E=corridors)

def show_results(labyrinth: UndirectedGraph):
    print(labyrinth)

if __name__ == "__main__":
    rows, cols = read_data(sys.stdin)
    labyrinth = process(rows, cols)
    show_results(labyrinth)
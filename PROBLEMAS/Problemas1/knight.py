import sys
from random import shuffle

from algoritmia.datastructures.digraphs import UndirectedGraph
from typing import *

from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.queues import Fifo

from labyrinth import create_labyrinth

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]


def knight_graph(rows: int, cols: int) -> UndirectedGraph:
    vertices = [(r, c) for r in range(rows) for c in range(cols)]

    mfs = MergeFindSet()
    for v in vertices: mfs.add(v)

    edges= []
    for r in range(rows):
        for c in range(cols):
            if r + 1 < rows and c + 2 < cols:
                edges.append(((r, c), (r + 1, c + 2)))
            if r + 1 < rows and c - 2 >= 0:
                edges.append(((r, c), (r - 1, c - 2)))

            if r + 2 < rows and c + 1 < cols:
                edges.append(((r, c), (r + 2, c + 1)))

            if r + 2 < rows and c - 1 >= 0:
                edges.append(((r, c), (r + 2, c + 1)))

    shuffle(edges)

    return UndirectedGraph(E=edges)


def read_data(f) -> Tuple[int, int, int, int]:
    rows = f.readline()
    cols = f.readline()
    first_row = f.readline()
    first_col = f.readline()
    return (int(rows), int(cols), int(first_row), int(first_col))


def show_data(n: int):
    print(n)


def process(rows: int, cols: int, first_row: int, first_col: int) -> int:
    g = knight_graph(rows, cols)

    la = df_search(g, (first_row, first_col))

    return len(la)-1


def df_search(g: UndirectedGraph, target: Vertex) -> List[Edge]:
    def recorrido_desde(u,v):
        seen.add(v)
        aristas.append((u,v))
        for suc in g.succs(v):
            if suc not in seen:
                recorrido_desde(v,suc)

    aristas = []
    seen = set()
    recorrido_desde(target, target)
    return aristas


if __name__ == '__main__':

    rows, cols, first_row, first_col = read_data(sys.stdin)
    n = process(rows, cols, first_row, first_col)
    show_data(n)



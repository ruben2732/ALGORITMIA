import sys
from typing import *
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo

from labyrinth import create_labyrinth


Vertex=Tuple[int,int]
Edge= Tuple[Vertex, Vertex]
Path=List[Vertex]

def bf_search(g: UndirectedGraph, source: Vertex, target: Vertex) -> List[Edge]:
    aristas = []
    queue = Fifo()
    seen = set()
    queue.push((source, source))
    seen.add(source)
    while len(queue)>0:
        u, v = queue.pop()
        aristas.append((u, v))
        if v==target:
            return aristas
        for suc in g.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push((v, suc))
    return aristas


#Recorredor aristas en profundidad, versión que para
def df_search(g: UndirectedGraph, source: Vertex, target: Vertex) -> List[Edge]:
    def recorrido_desde(u,v):
        seen.add(v)
        aristas.append((u,v))
        if v==target:
            return
        for suc in g.succs(v):
            if suc not in seen:
                recorrido_desde(v,suc)

    aristas = []
    seen = set()
    recorrido_desde(source, source)
    return aristas


    #recuperador_camino
def recover_path(edges: List[Edge], target: Vertex) -> Path:

    bp={}
    for(p,h) in edges:
        bp[h]=p
    v=target
    camino=[v]
    while v!=bp[v]:
        v=bp[v]
        camino.append(v)
    camino.reverse()
    return camino

def read_data(f) -> Tuple[int,int]:
    rows=int(f.readline())
    cols=int(f.readline())
    return (rows, cols)

def process(rows: int, cols: int) -> Tuple[UndirectedGraph, Path]:
    g=create_labyrinth(rows, cols, int(rows*cols*0.4))


    la = bf_search(g, (0,0), (rows-1,cols-1))
    path= recover_path(la, (rows-1,cols-1))

    return (g,path)


def show_results(path: Path):
    for v in path:
        print(v)


if __name__ == '__main__':

    rows, cols= read_data(sys.stdin)
    g, path = process(rows,cols)
    show_results(path)
















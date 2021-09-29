import sys

from algoritmia.datastructures.digraphs import UndirectedGraph

from PROBLEMAS.Problemas1.knight import knight_graph
from graph2dviewer import Graph2dViewer


def read_data(f):
    rows=f.readline()
    cols=f.readline()
    return int(rows),int(cols)

def process(rows, cols):
    return knight_graph(rows,cols)


def show_data(g: UndirectedGraph):
    viewer = Graph2dViewer(g, vertexmode=Graph2dViewer.ROW_COL)
    viewer.run()


if __name__ == '__main__':

    rows, cols = read_data(sys.stdin)
    n = process(rows, cols)
    show_data(n)
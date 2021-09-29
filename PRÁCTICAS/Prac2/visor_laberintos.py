from Utils.labyrinthviewer import LabyrinthViewer
from creador_laberintos import process

if __name__ == "__main__":
    cols = 150
    rows = 60
    labyrinth = process(rows, cols)
    lv = LabyrinthViewer(labyrinth,
                         canvas_width=10 * cols,
                         canvas_height=10 * rows)
    lv.run()
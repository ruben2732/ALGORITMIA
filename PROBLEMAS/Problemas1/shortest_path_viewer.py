from shortest_path import process
from labyrinthviewer import LabyrinthViewer


if __name__ == "__main__":
    cols = 60
    rows = 40
    g , path= process(rows, cols)

    lv = LabyrinthViewer( g,canvas_width=10 * cols,
                         canvas_height=10 * rows, margin=10)
    lv.add_path(path, color="blue")
    #lv.add_path(path, offset=2, color="red")
    lv.run()
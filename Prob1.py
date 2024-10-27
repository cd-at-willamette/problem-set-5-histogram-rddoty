#Reagan Doty

from pgl import GWindow, GCompound, GRect

n = 10
sample = [3, 4, 3, 5, 1, 2, 4, 3, 6, 7, 6, 8, 9, 0, 6, 8, 9]

#1a
def create_histogram_array(n, samples):
    """Returns a histogram array from samples with values in range(0, n)."""
    counts_list = [0] * n
    for i in range(len(samples)):
        if samples[i] < n:
            counts_list[samples[i]] += 1
    return(counts_list)

#1b
def print_histogram(array):
    """Prints a rotated histogram of array on the console."""
    for i in range(len(array)):
        line = ""
        line = array[i] * "*"
        print(line)

#1c
def create_histogram_graph(array, width, height):
    """Returns a GCompound that graphs the histogram array."""
    graph = GCompound()
    max_number = max(array)
    for i in range(len(array)):
        square = GRect(width/len(array), height / max_number * array[i])
        square.set_fill_color("Pink")
        square.set_filled(True)
        graph.add(square, i* width/len(array), height-(height / max_number * array[i]))
    return graph


GWINDOW_WIDTH = 700
GWINDOW_HEIGHT = 400


def create_histogram_graph_test():
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    array = create_histogram_array(n, sample)
    graph = create_histogram_graph(array, GWINDOW_WIDTH, GWINDOW_HEIGHT)
    gw.add(graph)


if __name__ == "__main__":
    print(create_histogram_array(n, sample))
    counts = create_histogram_array(n, sample)
    print_histogram(counts)
    create_histogram_graph_test()

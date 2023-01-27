n = 3
N = n * n
def box_index(row, col): return (row // n) * n + col // n


print(box_index)

def flood_fill(matrix: list, starting_cell: tuple, new_color: int) -> list:
    '''Any image can be represented by a 2D integer array (i.e., a matrix) where each cell represents the pixel value of the image.
Flood fill algorithm takes a starting cell (i.e., a pixel) and a color. The given color is applied to all horizontally and vertically connected cells with the same color as that of the starting cell. Recursively, the algorithm fills cells with the new color until it encounters a cell with a different color than the starting cell. 
Given a matrix, a starting cell, and a color, flood fill the matrix.'''

    rows = len(matrix)
    cols = len(matrix[0])
    target = matrix[starting_cell[0]][starting_cell[1]]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == target:
                dfs(matrix, i, j, new_color, target)
    return matrix


def dfs(matrix, x, y, color, target):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return
    if matrix[x][y] == target:
        matrix[x][y] = color

        dfs(matrix, x - 1, y, color, target)
        dfs(matrix, x + 1, y, color, target)
        dfs(matrix, x, y - 1, color, target)
        dfs(matrix, x, y + 1, color, target)

    else:
        return


input_matrix = [[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
    0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]
start_cell = (1, 3)
color = 2
print(flood_fill(input_matrix, start_cell, color))

# iterate through row
# iterate through column
# if cell == starting cell,
# check neighbors, convert to new color, recursively

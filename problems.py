## Constants
# Array of index offsets to find adjacent cells in rectangular grid
ADJACENT_INDEX_OFFSETS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1) 
]

class GridNotValidError(Exception):
    """
    Exception class to be raised when grid is not a valid rectangle
    """
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return repr(self.value)

def validate_grid_index(grid, index):
    """
    Take a rectangular grid of numbers and a tuple index and check 
    if the index (r,c) is valid inside of it.
    Returns True if index is valid.
    """
    
    # index[0] is the row and index[1] is the column
    if index[0] >= 0 and index[1] >= 0 and index[0] < len(grid) and index[1] < len(grid[0]):
        return True
    return False

def get_subsequence_length(grid, path):
    """
    Take a rectangular grid of numbers and a subsequence through it and
    find the length of that subsequence through the 
    grid recursing until the end is reached.
    Path is only valid if difference between value and neighbour is > 3.
    Returns length of subsequence as integer.
    """
    
    # Get the last val in the path
    row = path[-1][0]
    col = path[-1][1]
    
    currentVal = grid[row][col]

    for cell in ADJACENT_INDEX_OFFSETS:
        index = (row + cell[0], col + cell[1])
        if validate_grid_index(grid, index) and index not in path and abs(grid[index[0]][index[1]] - currentVal) > 3:
            path.append(index)
            return get_subsequence_length(grid, path)

    return len(path)
    
def longest_subsequence(grid):
    """
    Take a rectangular grid of numbers and find the length
    of the longest sequence.
    Return the length as an integer.
    """
    
    # Validate against constraints in instructions and definition of a rectangle (parallel sides equal)
    if len(grid) < 1 or len(grid) > 10: 
        raise GridNotValidError("Grid must have between 1 and 10 rows")
    for row in grid[1:]:
        if len(row) < 1 or len(row) > 10 or len(row) != len(grid[0]):
            raise GridNotValidError("Grid must have between 1 and 10 columns and they must all be the same length")
      
    max_length = 0
    for r, rowVal in enumerate(grid):
        for c, colVal in enumerate(rowVal):
            # start path with this index
            length = get_subsequence_length(grid, [(r, c)])
            if (length > max_length):
                max_length = length
    
    return max_length


grid = [[4,2,4], [0,3,1], [3,7,9]]
longestPath = longest_subsequence(grid)
print(longestPath)
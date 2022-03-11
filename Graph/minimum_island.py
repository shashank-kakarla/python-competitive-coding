from xmlrpc.client import MAXINT


# def minimum_island(grid):
#     visited = set()
#     smallest = MAXINT
#     for row in range(0,len(grid)):
#         for col in range(0,len(grid[0])):
#             if grid[row][col] == 'L' and (row,col) not in visited:
#                 size = explore_island(grid, row, col, visited)
#                 smallest = size if size < smallest else smallest
#     return smallest

def minimum_island(grid):
    visited = set()
    smallest = MAXINT
    for row in range(0,len(grid)):
        for col in range(0,len(grid[0])):
            size = explore_island(grid, row, col, visited)
            smallest = size if size >0 and size< smallest else smallest
    return smallest

def explore_island(grid, row, col, visited):
    size = 0
    row_bound = 0 <= row < len(grid)
    col_bound = 0 <= col < len(grid[0])
    if not row_bound or not col_bound or grid[row][col] == 'W':
        return 0
    
    if grid[row][col] == 'L' and (row,col) not in visited:
        visited.add((row,col))
        size+=1
        size+=explore_island(grid,row-1,col,visited)
        size+=explore_island(grid,row+1,col,visited)
        size+=explore_island(grid,row,col-1,visited)
        size+=explore_island(grid,row,col+1,visited)
    
    return size

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(minimum_island(grid))
def island_count(grid):
    count =0
    visited = set()
    for row in range(0, len(grid)):
        for col in range(0,len(grid[0])):
            if grid[row][col] == 'L' and (row,col) not in visited:
                count+=1
                explore_land(grid, row, col, visited)
            else:
                continue
    
    return count

def explore_land(grid, row, col, visited):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 'W':
        return
    if grid[row][col] == 'L' and (row,col) not in visited:
        visited.add((row,col))
        explore_land(grid,row-1,col,visited)
        explore_land(grid,row+1,col,visited)
        explore_land(grid,row,col-1,visited)
        explore_land(grid,row,col+1,visited)

# def explore_land(grid, row, col, visited):
#     if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
#         return
#     elif grid[row][col] == 'L' and (row,col) not in visited:
#         visited.add((row,col))
#     else:
#         return
#     explore_land(grid,row-1,col,visited)
#     explore_land(grid,row+1,col,visited)
#     explore_land(grid,row,col-1,visited)
#     explore_land(grid,row,col+1,visited)


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(island_count(grid))
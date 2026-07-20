import copy
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        newGrid = copy.deepcopy(grid)
        rowNum = len(grid)
        colNum = len(grid[0])
        for row in range(rowNum):
            for col in range(colNum):
                newGrid[(row + (col + k)//colNum)%rowNum][(col + k)%colNum] = grid[row][col]
        
        return newGrid

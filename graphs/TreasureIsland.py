'''
Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
'''

grid_map = [['O', 'O', 'O', 'O'],
            ['D', 'O', 'D', 'O'],
            ['O', 'O', 'O', 'O'],
            ['X', 'D', 'D', 'O']]

class TreasureIsland:
    def __init__(self, grid_map):
        self.grid = grid_map
        self.max_row = len(grid_map)
        self.max_column = len(grid_map[0])
    
    def out(self):
        print(self.max_row)
        print(self.max_column)
    
    def isLocationValid(self, row_id, column_id):
        if row_id < self.max_row and column_id < self.max_column and row_id >= 0 and column_id >=0 and self.grid[row_id][column_id]!='D':
            return True
        return False
    
    
    UP = [0,1]
    DOWN = [0,-1]
    LEFT = [-1,0]
    RIGHT = [1,0]
    Directions = [UP, DOWN, LEFT, RIGHT]
    
    def findTreasure(self):
        visited_coordinates = [] 
        # A queue of paths
        queue_coordinates = []
        start = (0,0)
        steps = 0
        visited_coordinates.append(start)
        queue_coordinates.append([start])
        while queue_coordinates:
            #Get the first path
            path = queue_coordinates.pop(0)
            # Get the last coordinate from the path
            row_id, column_id = path[-1]
            if(self.grid[row_id][column_id]) == 'X':
                return path
                
            for sail in self.Directions:
                new_path = list(path)
                c_row_id = row_id + sail[0]
                c_column_id = column_id + sail[1]
                
                if self.isLocationValid(c_row_id, c_column_id):
                    if (c_row_id, c_column_id) not in visited_coordinates:
                        #print("new location: ", c_row_id, c_column_id)
                        #print("Found: ", self.grid[c_row_id][c_column_id])
                        visited_coordinates.append((c_row_id, c_column_id))
                        new_path.append((c_row_id, c_column_id))
                        queue_coordinates.append(new_path)  
                        
TI1 = TreasureIsland(grid_map)
TI1.out()
Shortest_Path = TI1.findTreasure()
print("Shortest_Path:", Shortest_Path)
print("Steps taken:", len(Shortest_Path)-1)
"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import random

class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m-1 and columns are numbered 0..n-1.
    """
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The intiail state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state

    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

    def is_sorted(self):
        """
        Checks is the current state of the grid is sorted and returns the answer as a boolean.
        """
        result=[]
        for i in range (self.m):
            result = result + self.state[i]
        for k in range (len(result)-1):
            if result[k]>result[k+1]:
                return False
            return True
                
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        raise NotImplementedError
    
    def right_pos(self, cell):
        if state[cell[0]][cell[1]]==n*cell[0]+cell[1]+1:
            return True
        return False

    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        posc1=[cell1[0],cell1[1]]
        posc2=[cell2[0],cell2[1]]

        if cell1[0]==cell2[0]:
            if cell1[1]==cell2[1]+1 or cell1[1]==cell2[1]-1 or cell1[1]==cell2[1]: 
                self.state[cell1[0]][cell1[1]]=self.state[posc2[0]][posc2[1]]
                self.state[cell2[0]][cell2[1]]=self.state[posc1[0]][posc1[1]]
        elif cell1[1]==cell2[1]:
            if cell1[0]==cell2[0]+1 or cell1[0]==cell2[0]-1 or cell1[0]==cell2[0]:
                self.state[cell1[0]][cell1[1]]=self.state[posc2[0]][posc2[1]]
                self.state[cell2[0]][cell2[1]]=self.state[posc1[0]][posc1[1]]
        else:
            raise ValueError


    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        for k in range (len(cell_pair_list)):
            swap(cell_pair_list[k][0],cell_pair_list[k][1])

    

    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid



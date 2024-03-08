"""
This is the grid module. It contains the Grid class and its associated methods.
"""
from functools import reduce


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
    
    def __init__(self, m, n, initial_state=[]):
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
    
 
    
    def liste_to_condensat(self): # fonction qui permet de transformer une liste en un hashable à l'aide de la fonction reduce et de lambda #
        """
        Turns a list (of list) into a condensat.
        This allows to use graph methods with a swap puzzle graph
        """

        result=[]
        for i in range (self.m):
           result = result + self.state[i]
        #print(tuple(result))

        final_tuple=tuple(result)
        key_word=str(self.m)+"a"+str(self.n)

        for k in range(len(final_tuple)): 
            #print(final_tuple[k])
            key_word=key_word+"a"+str(final_tuple[k])
        #result_int = reduce(lambda acc, digit: acc * 10 + digit, final_tuple) #méthode de transformation d'un tuple vers un entier

        return key_word

    def condensat_to_grid(condensat): #réciproque ok !
        print(condensat)
        first_liste=condensat.split("a")
        print(first_liste)
        
        m=int(first_liste.pop(0))
        n=int(first_liste.pop(1))

        ligne=[]
        matrice=[]

        for i in range(m):
            ligne=[]
            for j in range(i*n,(i+1)*n-1):
                ligne.append(first_liste[j])
                print(ligne)
            matrice.append(ligne)

        print(m)
        print(n)
        result=Grid(m,n,matrice)
        print(result)


    def is_sorted(self):# fonction qui vérifie si les éléments de la grille sont bien ordonnés et qui retourne vrai ou faux en fonction #
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

    def swap(self, cell1, cell2):# fonction de swap entre deux cellules si et seulement si elles sont adjacentes #
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        c1=self.state[cell1[0]][cell1[1]]
        c2=self.state[cell2[0]][cell2[1]]

        if cell1[0]==cell2[0]:
            if cell1[1]==cell2[1]+1 or cell1[1]==cell2[1]-1 or cell1[1]==cell2[1]: 
                self.state[cell1[0]][cell1[1]]=c2
                self.state[cell2[0]][cell2[1]]=c1
        elif cell1[1]==cell2[1]:
            if cell1[0]==cell2[0]+1 or cell1[0]==cell2[0]-1 or cell1[0]==cell2[0]:
                self.state[cell1[0]][cell1[1]]=c2
                self.state[cell2[0]][cell2[1]]=c1
        else:
            raise ValueError


    def swap_seq(self, cell_pair_list):# fonction qui exécute une liste de swap, en rapport à la fonction définie ci-dessus #
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

    def voisin(self): #détermine tous les voisins d'une grille et retourne une liste de hash
        neighbors=[]
        for i in range(self.m-1):
            for j in range(self.n-1):              
                self.swap((i,j),(i+1,j))
                neighbors.append(self.liste_to_condensat())
                print(self.state)
                self.swap((i,j),(i+1,j))
                self.swap((i,j),(i,j+1))
                neighbors.append(self.liste_to_condensat())
                print(self.state)
                self.swap((i,j),(i,j+1))
        for i in range (self.m-1):
            self.swap((i,self.n-1),(i+1,self.n-1))
            neighbors.append(self.liste_to_condensat())
            print(self.state)
            self.swap((i,self.n-1),(i+1,self.n-1))
        for j in range (self.n-1):
            self.swap((self.m-1,j),(self.m-1,j+1))
            neighbors.append(self.liste_to_condensat())
            print(self.state)
            self.swap((self.m-1,j),(self.m-1,j+1))
        print(len(neighbors))
        return neighbors
    
    def distance(self,dst):
        
        #if isinstance(dst, str):
        #    Grid.condensat_to_grid()
        distance = 0
        for i in range (self.m):
            for j in range (self.n):
                if self.state[i][j] != dst.state[i][j]:
                    distance += 1
        return distance




    def bfs_final(self,src,dst):# fonction bfs appliquée à la grille, chaque noeud étant un état de la grille et chaque arête correspond à un swap #
        
        visited_condensats=[]
        waiting_list=[[src]]

        if src==dst:
            print("Espèce d'abruti c'est les mêmes grilles")
        
        while wainting_list != []:
            path=wainting_list.pop(0)
            node=path[-1]

            if node==dst:
                visited_condensats.append(node)
                return path
            neighbours = self.graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                

            
            

            neighbours=[]



        
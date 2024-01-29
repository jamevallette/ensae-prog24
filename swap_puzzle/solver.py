from grid import Grid
from random import *

class Solver(): 
    """
    A solver class, to be implemented.
    """
    def get_solution(self):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """       
        compteur=0
        for k in range(1,n*m+1):
            i_start=0
            j_start=0
            for i in range(n):
                for j in range(m):
                    if state[i][j]==k:
                        i_start=i
                        j_start=j
                    else:
                        raise ValueError
            if (k-1)//n==i_start:
                if j_start>(k-1)%n:
                    while j_start>(k-1)%n:
                        swap((i_start,j_start),(i_start,j_start-1))
                if j_start<(k-1)%n:
                    while j_start<(k-1)%n:
                        swap((i_start,j_start),(i_start,j_start+1))
            elif (k-1)%n==j_start:
                if i_start>(k-1)//n:
                    while i_start>(k-1)//n:
                        swap((i_start,j_start),(i_start-1,j_start))
                if i_start<(k-1)//n:
                    while i_start>(k-1)//n:
                        swap((i_start,j_start),(i_start+1,j_start))
            else:
                if j_start>(k-1)%n:
                    while j_start>(k-1)%n:
                        swap((i_start,j_start),(i_start,j_start-1))
                        compteur=compteur+1
                    if i_start>(k-1)//n:
                        while i_start>(k-1)//n:
                            swap((i_start,j_start),(i_start-1,j_start))
                            compteur=compteur+1
                    elif i_start<(k-1)//n:
                        while i_start>(k-1)//n:
                            swap((i_start,j_start),(i_start+1,j_start))
                            compteur=compteur+1
                elif j_start<(k-1)%n:
                    while j_start<(k-1)%n:
                        swap((i_start,j_start),(i_start,j_start+1))
                        compteur=compteur+1
                    if i_start>(k-1)//n:
                        while i_start>(k-1)//n:
                            swap((i_start,j_start),(i_start-1,j_start))
                            compteur=compteur+1
                    elif i_start<(k-1)//n:
                        while i_start>(k-1)//n:
                            swap((i_start,j_start),(i_start+1,j_start))
                            compteur=compteur+1
            print(compteur)
          
    

       
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        raise NotImplementedError


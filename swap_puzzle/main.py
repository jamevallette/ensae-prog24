
from grid import Grid
import heapq

data_path = "ensae-prog24/input/"

file_name = data_path + "grid5.in"
file_bis = data_path + "grid2_solved.in"

grid0_path= data_path + "grid0.in"
two_two_solved= Grid(2,2)

print(file_name)

g = Grid.grid_from_file(file_name)
h = Grid.grid_from_file(file_bis)
f = Grid.grid_from_file(grid0_path)



#print(g)
#print(g.grid_to_condensat())
#print(g.voisin())
#print(Grid(2,2).voisin())
#print(Grid.condensat_to_grid(g.grid_to_condensat()))
#print(g.distance(h))
#print(Grid.bfs_final(g,h))
print(g.solver_Astar())
#print(g.solver_bfs())

"""first_liste[0]
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,1)
for i in range(0,n):
    for j in range(0,m):
        data = (i,j)
        ax.axis("tight")
        ax.axis("off")
        ax.table(cellText=data, loc="center")


plt.show()
"""



"""
from graph import Graph
data_path = "ensae-prog24/input/"
file_name=data_path + "graph2.in"
test = Graph.graph_from_file(file_name)
print(test)



print(test.bfs(4,19))
"""
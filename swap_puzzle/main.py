
from grid import Grid

data_path = "ensae-prog24/input/"
file_name = data_path + "grid1.in"

print(file_name)

g = Grid.grid_from_file(file_name)

print(g)
#print(g.voisin())
print(Grid.condensat_to_grid(g.m,g.n,g.liste_to_condensat()))

"""
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
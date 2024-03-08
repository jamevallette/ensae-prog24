
from grid import Grid

data_path = "ensae-prog24/input/"
file_name = data_path + "grid2.in"
file_bis = data_path + "grid2_bis.in"
print(file_name)

g = Grid.grid_from_file(file_name)
h = Grid.grid_from_file(file_bis)

print(g)
print(g.liste_to_condensat())

print(Grid.condensat_to_grid(g.liste_to_condensat()))
#print(g.distance(h))

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
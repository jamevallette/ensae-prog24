
from grid import Grid

g = Grid(2, 3)
print(g)
print(g.liste_to_condensat())

data_path = "ensae-prog24/input/"
file_name = data_path + "grid3.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)
print(g.liste_to_condensat())
print(tuple(5274163905634126))
"""
from graph import Graph
data_path = "ensae-prog24/input/"
file_name=data_path + "graph2.in"
test = Graph.graph_from_file(file_name)
print(test)



print(test.bfs(4,19))
"""
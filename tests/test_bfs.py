# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid

class Test_GridLoading(unittest.TestCase):
    def bfs_grid3(self):
        grid3 = Grid.grid_from_file("input/grid3.in")
        self.assertEqual(bfs(),9)
        self.assertEqual(grid2.distance(grid1), 9)
        self.assertEqual(grid1.distance(grid1), 0)
    
    def test_grid3_solved(self):
        grid3 = Grid.grid_from_file("input/grid3.in")
        grid3_solved = Grid(4,4)
        self.assertEqual(grid3.distance(grid3_solved),8)
        


if __name__ == '__main__':
    unittest.main()

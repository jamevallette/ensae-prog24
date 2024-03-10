# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid

class Test_GridLoading(unittest.TestCase):
    def bfs_grid3(self):
        grid3 = Grid.grid_from_file("input/grid3.in")
        expected_result="The grid is in the following state: \n[5, 2, 7, 4]\n[1, 6, 3, 8]\n[9, 14, 15, 12]\n[13, 10, 11, 16]\n\nThe grid is in the following state:\n[1, 2, 7, 4]\n[5, 6, 3, 8]\n[9, 14, 15, 12]\n[13, 10, 11, 16]\n\nThe grid is in the following state:\n[1, 2, 3, 4]\n[5, 6, 7, 8]\n[9, 14, 15, 12]\n[13, 10, 11, 16]\n\nThe grid is in the following state:\n[1, 2, 3, 4]\n[5, 6, 7, 8]\n[9, 10, 15, 12]\n[13, 14, 11, 16]\n\nThe grid is in the following state:\n[1, 2, 3, 4]\n[5, 6, 7, 8]\n[9, 10, 11, 12]\n[13, 14, 15, 16]\n\n['4a4a5a2a7a4a1a6a3a8a9a14a15a12a13a10a11a16', '4a4a1a2a7a4a5a6a3a8a9a14a15a12a13a10a11a16', '4a4a1a2a3a4a5a6a7a8a9al4al5al2al3al0a11al6','4a4a1a2a3a4a5a6a7a8a9a10a15a12a13al4a11a16', '4a4a1a2a3a4a5a6a7a8a9a10a11a12a13a14a15a16']"
        self.assertEqual(Grid.bfs_final(grid3,Grid(4,4)),expected_result)

if __name__ == '__main__':
    unittest.main()
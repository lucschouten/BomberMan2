import numpy as np
import typing
import unittest

from assignment1 import BomberMan


class TestBomberMan(unittest.TestCase):

    @staticmethod
    def string_to_ndarray(world: str, dimensions: typing.Tuple) -> np.ndarray:
        result = np.zeros(dimensions)
        if dimensions[0] * dimensions[1] != len(world):
            raise ValueError()
        for idx, i in enumerate(world):
            if i == 'X':
                number = 1
            elif i == '+':
                number = 2
            elif i == ' ':
                number = 0
            else:
                raise ValueError('Unexpected str value: %s' % i)
            y_pos = int(idx/dimensions[1])
            x_pos = idx % dimensions[1]
            result[y_pos, x_pos] = number
        return result

    @staticmethod
    def get_world_greedy() -> BomberMan:
        world_str = \
            "XXXXXXX" + \
            "X     X" + \
            "X +++ X" + \
            "X  +  X" + \
            "X     X" + \
            "XXXXXXX"
        dimensions = (6, 7)
        world_array = TestBomberMan.string_to_ndarray(world_str, dimensions)
        return BomberMan(world_array)

    @staticmethod
    def get_world_walls() -> BomberMan:
        world_str = \
            "XXXXXXXXXXX" + \
            "X +     + X" + \
            "X+X X+X X+X" + \
            "X    +    X" + \
            "X+X X+X X+X" + \
            "X +     + X" + \
            "XXXXXXXXXXX"
        dimensions = (7, 11)
        world_array = TestBomberMan.string_to_ndarray(world_str, dimensions)
        return BomberMan(world_array)

    def test_aux_functions_greedyworld(self):
        bomberman = TestBomberMan.get_world_greedy()

        self.assertEqual(4, bomberman.number_of_crates())
        self.assertFalse(bomberman.is_final_state())

    def test_crate_functions_greedyworld(self):
        bomberman = TestBomberMan.get_world_greedy()
        self.assertEqual({(3, 3), (2, 2)}, bomberman.crates_in_range(3, 2))
        self.assertEqual({(3, 3), (2, 4)}, bomberman.crates_in_range(3, 4))

    def test_move_functions_greedyworld(self):
        bomberman = TestBomberMan.get_world_greedy()
        self.assertEqual(16, len(bomberman.reachable_positions(1, 3)))
        self.assertEqual(6, len(bomberman.determine_unequivalent_moves(1, 3)))

    def test_optimize_function_greedyworld(self):
        bomberman = TestBomberMan.get_world_greedy()
        optimal = bomberman.number_bombs_optimal(1, 3)
        self.assertEqual(2, optimal)

    def test_greedy_function_greedyworld(self):
        bomberman = TestBomberMan.get_world_greedy()
        greedy = bomberman.number_bombs_greedy(1, 3)
        self.assertEqual(3, greedy)

    def test_aux_functions_wallworld(self):
        bomberman = TestBomberMan.get_world_walls()
        self.assertEqual(11, bomberman.number_of_crates())
        self.assertFalse(bomberman.is_final_state())

    def test_crate_functions_wallworld(self):
        bomberman = TestBomberMan.get_world_walls()
        self.assertEqual({(1, 2), (2, 1)}, bomberman.crates_in_range(1, 1))
        self.assertEqual({(1, 2), (2, 5), (1, 8)},
                         bomberman.crates_in_range(1, 5))
        self.assertEqual(set(), bomberman.crates_in_range(2, 7))

    def test_move_functions_wallworld(self):
        bomberman = TestBomberMan.get_world_walls()
        self.assertEqual(22, len(bomberman.reachable_positions(1, 5)))
        self.assertEqual(7, len(bomberman.determine_unequivalent_moves(1, 5)))

    def test_greedy_functions_wallworld(self):
        bomberman = TestBomberMan.get_world_walls()
        greedy = bomberman.number_bombs_greedy(1, 5)
        self.assertEqual(4, greedy)

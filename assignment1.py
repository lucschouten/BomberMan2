import numpy as np
import typing


class BomberMan(object):

    def __init__(self, state: np.ndarray) -> None:
        """
        Initializes the class with the initial state. As parameter, we obtain a
        2D numpy array of type int. Here, a 0 represents an empty spot, a 1
        represents a wall (which can not explode), and a 2 represents a crate.
        There will not be any other numbers in the array.

        :param state: the Initial state
        """
        self.state = state

    def __str__(self):
        """
        Represents the current state as string

        :return: the current state as string.
        """
        result = ""
        for y_pos in range(len(self.state)):
            for x_pos in range(len(self.state[y_pos])):
                current = self.state[y_pos, x_pos]
                if current == 0:
                    result += ' '
                elif current == 1:
                    result += 'X'
                elif current == 2:
                    result += '+'
                else:
                    raise ValueError('Unexpected value in state: %s' % current)
            result += '\n'
        return result

    def number_of_crates(self) -> int:
        """
        Returns the number of crates in the current game state

        :return: number of crates
        """

    def is_final_state(self) -> bool:
        """
        Returns whether the current state is the final state

        :return: True iff there are no crates, False otherwise
        """

    def crates_in_range(self, y_pos: int, x_pos: int) -> \
            typing.Set[typing.Tuple[int, int]]:
        """
        Determines for a bomb at a given position (x_pos, y_pos) which crates
        will be affected by an explosion. Note that an explosion goes through
        empty spots, the player and the first crate it fiends in a given
        direction, but not through walls.

        :param y_pos: the y position where the bomb is supposed to explode
        :param x_pos: the x position where the bomb is supposed to explode
        :return: A Set of Tuples. Each tuple represents a position of a crate
        that will be removed by the bomb, an consists of two integers, i.e., the
        y position and the x position (resp)
        """

    def detonate_bomb(self, y_pos: int, x_pos: int) -> None:
        """
        Transitions the state to the state that would be when a bomb explodes
        at position (x_pos, y_pos)

        :param x_pos: the x position where the bomb is supposed to explode
        :param y_pos: the y position where the bomb is supposed to explode
        """

    def reachable_positions(self, y_pos: int, x_pos: int) -> \
            typing.Set[typing.Tuple[int, int]]:
        """
        Determines the positions that can be reached from a given position. Note
        that the player can not walk through walls or crates, and not all
        positions might be reachable from the beginning.

        :param y_pos: The y position of the player
        :param x_pos: The x position of the player
        :return: A Set of Tuples. Each tuple consists of two integers, i.e., the
        x position and the y position of a position where the player can arrive
        """

    def determine_unequivalent_moves(self, y_pos: int, x_pos: int) -> \
            typing.Set[typing.Tuple[int, int]]:
        """
        Determines all moves that result in a unique state (i.e., the moves that
        are unequivalent)

        :param y_pos: The y position of the player
        :param x_pos: The x position of the player
        :return: A Set of Tuples. Each tuple consists of two integers, i.e., the
        x position and the y position of that move
        """

    def number_bombs_optimal(self, y_pos: int, x_pos: int) -> int:
        """
        Uses a brute force algorithm to determine the optimal (minimal) number
        of bombs required to explode all crates.

        :param y_pos: The y position of the player
        :param x_pos: The x position of the player
        :return: The optimal (minimal) number of bombs, required to explode all
        crates
        """

    def number_bombs_greedy(self, y_pos: int, x_pos: int) -> int:
        """
        Uses the following greedy algorithm to determine an upperbound on the
        minimal number of bombs required to explode all crates. Note that this
        number is always at least as high as the return value of
        `number_bombs_optimal`. As criterion, this greedy algorithm places a
        bomb on a position that leaves the least number of crates after
        exploding. In case of a tie, select the position with the lowest y
        position. In case of still a tie, select the position with the lowest x
        position.

        :param y_pos: The y position of the player
        :param x_pos: The x position of the player
        :return: The number of bombs required to explode all crates (upper
        bound)
        """

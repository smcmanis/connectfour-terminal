import unittest
import console
import random

from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_default_board_width(self):
        self.assertEqual(len(self.board.columns), 7)

    def test_default_board_height(self):
        self.assertEqual(len(self.board.columns[0]), 6)

    def test_valid_moves_initially_include_all_columns(self):
        self.assertEqual(self.board.get_valid_moves(), list(range(self.board.width)))

    def test_origin_is_not_out_of_bounds_true(self):
        self.assertFalse(self.board.is_out_of_bounds(0, 0))

    def test_negative_x_is_out_of_bounds_true(self):
        self.assertTrue(self.board.is_out_of_bounds(-1, 0))

    def test_negative_y_is_out_of_bounds_true(self):
        self.assertTrue(self.board.is_out_of_bounds(0, -1))

    def test_count_pieces_in_board(self):
        n = random.randint(1, 20)
        for i in range(n):
            self.board.drop_piece(random.randint(0, 6), random.randint(0, 1))

        self.assertEqual(self.board.pieces_in_board(), n)

    def test_drop_single_piece(self):
        self.setUp()
        self.board.drop_piece(1, 1)
        self.assertEqual(self.board.columns[1][0], 1)

    def test_drop_stacked_pieces(self):
        self.setUp()
        self.board.drop_piece(1, 1)
        self.board.drop_piece(1, 0)
        self.assertEqual(self.board.columns[1][1], 0)

    def test_is_connect_four_false_when_pieces_alternate(self):
        self.setUp()
        for i in range(4):
            self.board.drop_piece(i, i % 2)
        self.assertFalse(self.board.last_drop_makes_connectfour())

    def test_horizontal_connect_four(self):
        self.setUp()
        for i in range(4):
            self.board.drop_piece(i, 1)
        self.assertTrue(self.board.last_drop_makes_connectfour())

    def test_vertical_connect_four(self):
        self.setUp()
        for i in range(4):
            self.board.drop_piece(0, 1)
        self.assertTrue(self.board.last_drop_makes_connectfour())

    def test_horizontal_diagonal_connect_four(self):
        self.setUp()
        for i in range(4):
            self.board.drop_piece(i, 1)
            for j in range(i + 1):
                self.board.drop_piece(i + 1, (i + j) % 3 % 2)
        import console

        self.assertTrue(self.board.last_drop_makes_connectfour)


if __name__ == "__main__":
    unittest.main()

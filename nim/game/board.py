import random

# TODO: Define the Board class here

class Board:
    """ A board is defined as a designated playing surface. The responsibility of Board is to keep track of the pieces in play."""

    def __init__(self):

        """ Description here """
        self._board = []
        self._pile_board = []
        self._piles = 0
        self._stones = 0
        self._prepare()

    def apply(self, move):
        """ Description here
            Public method
        """
        pile_num = move.get_pile()

        for _ in range(move.get_stones()):
            self._board[pile_num].pop()

    def is_empty(self):
        """ Description here
            Public method
        """
        is_empty = None
        for i in range(len(self._board)):
            if len(self._board[i]) == 0:
                is_empty = True
            else:
                is_empty = False
                return is_empty  
        
        return is_empty
    
    def to_string(self):
        """ Description here
            Public method
        """
        print("--------------------")
        for pile in range(len(self._board)):
            print(f"{pile}: ", end = "")
            for stone in self._board[pile]:
                print(f"{stone} ", end = "")
            print()
        print("--------------------")

    def _prepare(self):
        """ Description here
            Private method
        """

        self._piles = random.randint(2, 5)

        for _ in range(self._piles):
            self._pile_board = []
            self._stones = random.randint(1, 9)
            for __ in range(self._stones):
                self._pile_board.append(0)
            self._board.append(self._pile_board)
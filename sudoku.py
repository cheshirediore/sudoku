class Board:
    """The sudoku board itself"""
    board = []

    def __init__(self):
        self.board = [[' ' for i in range(9)] for i in range(9)]

    def __str__(self):
        return ''.join(['+-------+-------+-------+\n'
            ,'\n+-------+-------+-------+\n'.join(['\n'.join(
                ['| {} | {} | {} |'.format(
                     ' '.join([str(self.get_row(row_num)[i]) for i in range(0,3)])
                    ,' '.join([str(self.get_row(row_num)[i]) for i in range(3,6)])
                    ,' '.join([str(self.get_row(row_num)[i]) for i in range(6,9)])
                ) for row_num in range(0,3)]
            )
            ,'\n'.join(
               ['| {} | {} | {} |'.format(
                    ' '.join([str(self.get_row(row_num)[i]) for i in range(0,3)])
                   ,' '.join([str(self.get_row(row_num)[i]) for i in range(3,6)])
                   ,' '.join([str(self.get_row(row_num)[i]) for i in range(6,9)])
               ) for row_num in range(3,6)]
           )
           ,'\n'.join(
              ['| {} | {} | {} |'.format(
                   ' '.join([str(self.get_row(row_num)[i]) for i in range(0,3)])
                  ,' '.join([str(self.get_row(row_num)[i]) for i in range(3,6)])
                  ,' '.join([str(self.get_row(row_num)[i]) for i in range(6,9)])
              ) for row_num in range(6,9)]
           )])
           ,'\n+-------+-------+-------+'])

    def get_column(self, column_num):
        return [x[column_num] for x in self.board]

    def get_row(self, row_num):
        return self.board[row_num]

    def get_block(self, block_num):
        """
        coordinate is a tuple (row, column). (0, 0) defines the top left block
        """
        # First Row
        if block_num == 1:
            coordinate = (0, 0)
        elif block_num == 2:
            coordinate = (3, 0)
        elif block_num == 3:
            coordinate = (6, 0)
        # Second Row
        elif block_num == 4:
            coordinate = (0, 3)
        elif block_num == 5:
            coordinate = (3, 3)
        elif block_num == 6:
            coordinate = (6, 3)
        # Third Row
        elif block_num == 7:
            coordinate = (0, 6)
        elif block_num == 8:
            coordinate = (3, 6)
        elif block_num == 9:
            coordinate = (6, 6)
        else:
            return None
        block = []
        for y in range(coordinate[0], coordinate[0]+3):
            for x in range(coordinate[1], coordinate[1]+3):
                block.append(self.board[x][y])
        return block

    def format_block(self, block_num):
        block = self.get_block(block_num)
        return '\n'.join([
                 ' | {} | '.format(' '.join([block[i] for i in range(0,3)]))
                ,' | {} | '.format(' '.join([block[i] for i in range(3,6)]))
                ,' | {} | '.format(' '.join([block[i] for i in range(6,9)]))
            ])

    def get_cell(self, x, y):
        """

        """
        return self.board[y][x]

    def set_cell(self, x, y, value):
        self.board[y][x] = value


class Cell:
    """A cell stores a value, with a boolean toggle"""
    value = None
    visible = None

    def __init__(self, value=0, visible=False):
        self.value = value
        self.visible = visible

    def __str__(self):
        if self.visible and self.value:
            return str(self.value)[0]
        else:
            return ' '


if __name__ == '__main__':
    board = [
       ['1','1','1','4','5','6','7','8','9']
      ,['1','1','1','4','5','6','7','8','9']
      ,['1','1','1','4','5','6','7','8','9']
      ,['1','2','3','4','5','6','7','8','9']
      ,['1','2','3','4','5','6','7','8','9']
      ,['1','2','3','4','5','6','7','8','9']
      ,['1','2','3','4','5','6','7','8','9']
      ,['1','2','3','4','5','6','7','8','9']
      ,['1','2','3','4','5','6','7','8','9']
    ]

    b = Board()

    print(b)
    b.board = board
    # print(b)

    # a = b.get_block(2)
    # print(b.format_block(2))

    print(b)
    b.set_cell(2,3,'a')
    print(b.get_cell(2,3))
    print(b)
    for x in range(0,9):
        for y in range(0,9):
            b.set_cell(x,y,' ')
    print(b)

# +-------+-------+-------+
# |       |       |       |
# |       |       |       |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |       |       |       |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |       |       |       |
# |       |       |       |
# +-------+-------+-------+

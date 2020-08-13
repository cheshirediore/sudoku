class Board:
    """The sudoku board itself"""
    board = []

    def __init__(self):
        self.board = [[Cell() for i in range(9)] for i in range(9)]

    def __str__(self):
        return ''.join(['+-------+-------+-------+\n'
            ,'\n+-------+-------+-------+\n'.join(['\n'.join(
              [self.format_row(self.get_row(row_num)) for row_num in range(0,3)]
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

    def format_row(self, row):
        return '| {} | {} | {} |'.format(
             ' '.join([str(row[i]) for i in range(0,3)])
            ,' '.join([str(row[i]) for i in range(3,6)])
            ,' '.join([str(row[i]) for i in range(6,9)])
        )

    def get_column(self, column_num):
        return [x[column_num] for x in self.board]

    def get_row(self, row_num):
        return self.board[row_num]

    def get_block(self, block_num):
        """
        coordinate is a tuple (row, column). (0, 0) defines the top left block
        """
        # First Row
        if block_num == 0:
            coordinate = (0, 0)
        elif block_num == 1:
            coordinate = (3, 0)
        elif block_num == 2:
            coordinate = (6, 0)
        # Second Row
        elif block_num == 3:
            coordinate = (0, 3)
        elif block_num == 4:
            coordinate = (3, 3)
        elif block_num == 5:
            coordinate = (6, 3)
        # Third Row
        elif block_num == 6:
            coordinate = (0, 6)
        elif block_num == 7:
            coordinate = (3, 6)
        elif block_num == 8:
            coordinate = (6, 6)
        else:
            print(block_num)
            return None
        block = []
        for y in range(coordinate[0], coordinate[0]+3):
            for x in range(coordinate[1], coordinate[1]+3):
                block.append(self.board[x][y])
        return block

    def get_cell(self, x, y):
        """

        """
        return self.board[y][x]

    def set_cell(self, x, y, value):
        self.board[y][x] = value

    def validate(self):
        # Validate Rows
        for i in range(9):
            # print('Row: %s' % (self.get_row(i)))
            if not self.subvalidate(self.get_row(i)):
                return False
        # Validate Columns
        for i in range(9):
            # print('Column: %s' % (self.get_column(i)))
            if not self.subvalidate(self.get_column(i)):
                return False
        # Validate Blocks
        for i in range(9):
            # print('Block: %s' % (self.get_block(i)))
            if not self.subvalidate(self.get_block(i)):
                return False
        return True

    def subvalidate(self, section):
        values = [cell.get_value() for cell in section]
        # print(set(values))
        # print({'1','2','3','4','5','6','7','8','9'})
        return set(values) == {'1','2','3','4','5','6','7','8','9'}

class Cell:
    """A cell stores a value, with a boolean toggle"""
    value = None
    visible = None

    def __init__(self, value=0, visible=False):
        self.value = value
        self.visible = bool(visible)

    def __str__(self):
        if self.visible and self.value:
            return str(self.value)[0]
        else:
            return ' '

    def __repr__(self):
        if self.value:
            return str(self.value)[0]
        else:
            return ' '

    def get_value(self):
        return str(self.value)

    def toggle(self):
        self.visible = not self.visible
        return self.visible


if __name__ == '__main__':
    board = [
         [Cell(value='5', visible=1), Cell(value='1', visible=0), Cell(value='3', visible=0), Cell(value='6', visible=0), Cell(value='8', visible=0), Cell(value='7', visible=0), Cell(value='2', visible=0), Cell(value='4', visible=1), Cell(value='9', visible=1)]
        ,[Cell(value='8', visible=0), Cell(value='4', visible=0), Cell(value='9', visible=0), Cell(value='5', visible=0), Cell(value='2', visible=0), Cell(value='1', visible=0), Cell(value='6', visible=0), Cell(value='3', visible=1), Cell(value='7', visible=0)]
        ,[Cell(value='2', visible=0), Cell(value='6', visible=1), Cell(value='7', visible=1), Cell(value='3', visible=0), Cell(value='4', visible=0), Cell(value='9', visible=0), Cell(value='5', visible=0), Cell(value='8', visible=0), Cell(value='1', visible=1)]
        ,[Cell(value='1', visible=1), Cell(value='5', visible=1), Cell(value='8', visible=0), Cell(value='4', visible=0), Cell(value='6', visible=0), Cell(value='3', visible=0), Cell(value='9', visible=0), Cell(value='7', visible=0), Cell(value='2', visible=0)]
        ,[Cell(value='9', visible=0), Cell(value='7', visible=0), Cell(value='4', visible=0), Cell(value='2', visible=0), Cell(value='1', visible=0), Cell(value='8', visible=0), Cell(value='3', visible=0), Cell(value='6', visible=0), Cell(value='5', visible=0)]
        ,[Cell(value='3', visible=0), Cell(value='2', visible=0), Cell(value='6', visible=0), Cell(value='7', visible=0), Cell(value='9', visible=0), Cell(value='5', visible=0), Cell(value='4', visible=0), Cell(value='1', visible=1), Cell(value='8', visible=1)]
        ,[Cell(value='7', visible=1), Cell(value='8', visible=0), Cell(value='2', visible=0), Cell(value='9', visible=0), Cell(value='3', visible=0), Cell(value='4', visible=1), Cell(value='1', visible=1), Cell(value='5', visible=1), Cell(value='6', visible=0)]
        ,[Cell(value='6', visible=0), Cell(value='3', visible=0), Cell(value='5', visible=0), Cell(value='1', visible=0), Cell(value='7', visible=0), Cell(value='2', visible=1), Cell(value='8', visible=0), Cell(value='9', visible=0), Cell(value='4', visible=0)]
        ,[Cell(value='4', visible=1), Cell(value='9', visible=1), Cell(value='1', visible=0), Cell(value='8', visible=0), Cell(value='5', visible=1), Cell(value='6', visible=0), Cell(value='7', visible=0), Cell(value='2', visible=0), Cell(value='3', visible=1)]
    ]

    b = Board()

    b.board = board
    print(b.validate())
    print(b)
    for x in range(0,9):
        for y in range(0,9):
            b.set_cell(x,y,' ')
    print(b)

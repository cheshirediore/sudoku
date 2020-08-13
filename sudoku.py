class Game:
    board = None

    def __init__(self, board=None,player=None):
        self.board = Board(board=board)

    def get_board(self):
        return self.board

    def process_move(self):
        x,y,mark = input('Enter Mark (format "x y value")> ').split(' ')
        board = self.get_board().get_cell(int(x), int(y)).add_mark(mark)

    def play(self):
        while not self.get_board().check_solution():
            print(self.get_board())
            try:
                self.process_move()
            except KeyboardInterrupt as e:
                exit('\nGame Ended by Player')
        print('Winner!')


class Board:
    """The sudoku board itself"""
    board = None

    def __init__(self, board=None):
        if board:
            self.board = board
        else:
            self.board = [[Cell() for i in range(9)] for i in range(9)]

    def __str__(self):
        return ''.join([
             ' x 0 1 2 | 3 4 5 | 6 7 8\n'
            ,'y+-------+-------+-------+\n'
            ,'\n+-------+-------+-------+\n'.join([
                     '\n'.join([self.format_row(row_num) for row_num in range(0,3)])
                    ,'\n'.join([self.format_row(row_num) for row_num in range(3,6)])
                    ,'\n'.join([self.format_row(row_num) for row_num in range(6,9)])
           ])
           ,'\n+-------+-------+-------+'
       ])

    def format_row(self, row_num):
        row = self.get_row(row_num)
        return '{0}| {1} | {2} | {3} |'.format(row_num
            ,' '.join([str(row[i]) for i in range(0,3)])
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
        return self.board[y][x]

    def set_board(self, board):
        self.board = board

    def set_cell_visibility(self, x, y, visible):
        cell = self.get_cell(x, y)
        if visible:
            return cell.reveal()
        else:
            return cell.hide()

    def toggle_cell_visibility(self, x, y):
        cell = self.get_cell(x, y)
        return cell.toggle()

    def reveal_all(self):
        for x in range(0,9):
            for y in range(0,9):
                self.set_cell_visibility(x, y, True)

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
        values = [str(cell.get_value()) for cell in section]
        # print(set(values))
        # print({'1','2','3','4','5','6','7','8','9'})
        return set(values) == {'1','2','3','4','5','6','7','8','9'}

    def check_solution(self):
        for x in range(0,9):
            for y in range(0,9):
                cell = self.get_cell(x, y)
                if not cell.check():
                    return False
        return True


class Cell:
    """A cell stores a value, with a boolean toggle"""
    value = None
    marks = None
    mark = None
    visible = None

    def __init__(self, value=0, visible=False):
        self.value = value
        self.visible = bool(visible)
        self.marks = set()
        self.mark = None

    def __str__(self):
        if self.visible and self.value:
            return str(self.get_value())[0]
        elif self.mark:
            return str(self.mark)
        else:
            return ' '

    # def __repr__(self):
    #     return str(self)

    def get_value(self):
        return self.value

    def get_marks(self):
        # return self.marks
        return self.mark

    def toggle(self):
        self.visible = not self.visible
        return self.visible

    def reveal(self):
        self.visible = True
        return self.visible

    def hide(self):
        self.visible = False
        return self.visible

    def add_mark(self, mark):
        # self.marks.add(mark)
        self.mark = mark

    def remove_mark(self, mark):
        # try:
        #     self.marks.remove(mark)
        # except KeyError as e:
        #     return False
        # else:
        #     return True
        self.mark = None

    def clear_marks(self):
        # self.marks.clear()
        self.mark = None

    def check(self):
        return self.get_value() == self.get_marks()



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
    game = Game(board=board)

    game.play()
    # b = Board(board)
    #
    # print(b.validate())
    # print(b)
    #
    # for x in range(0,9):
    #     for y in range(0,9):
    #         cell = b.get_cell(x, y)
    #         # cell.add_mark(cell.get_value())
    #         cell.add_mark(1)
    #
    # print(b)
    #
    # if b.check_solution():
    #     print('Winner!')
    # else:
    #     print('Not quite.')

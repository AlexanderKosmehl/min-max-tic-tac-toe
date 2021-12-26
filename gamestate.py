class gamestate:
    def __init__(self):
        self.grid = [[None for x in range(0, 3)] for x in range(0, 3)]

    def is_done(self):
        if self.check_winner() == "0":
            for row in self.grid:
                for cell in row:
                    if cell is None:
                        return False
        return True

    def check_winner(self):
        # Row Match
        for row in range(0, 3):
            row_set = set(self.grid[row])
            if len(row_set) == 1 and None not in row_set:

                return self.grid[row][0]

        # Column Match
        for column in range(0, 3):
            column_set = set([self.grid[column][0], self.grid[column][1], self.grid[column][2]])
            if len(column_set) == 1 and None not in column_set:
                return self.grid[0][column]

        # Diagonal Match
        diag1 = set([self.grid[0][0], self.grid[1][1], self.grid[2][2]])
        diag2 = set([self.grid[0][2], self.grid[1][1], self.grid[2][0]])

        if len(diag1) == 1 or len(diag2) == 1:
            if self.grid[1][1] is not None:
                return self.grid[1][1]

        return "0"

    def get_empty_cells(self):
        empty_cells = []
        for row in range(0, 3):
            for cell in range(0, 3):
                if self.grid[row][cell] is None:
                    empty_cells.append((row, cell))
        return empty_cells

    def print_gamestate(self):
        printable_state = gamestate()
        for row in range(0, 3):
            for cell in range(0, 3):
                if self.grid[row][cell] is None:
                    printable_state.grid[row][cell] = " "
                else:
                    printable_state.grid[row][cell] = self.grid[row][cell]

        print()
        print("   {0}  |  {1}  |  {2}   ".format(printable_state.grid[0][0], printable_state.grid[0][1],
                                                 printable_state.grid[0][2]))
        print("-------------------")
        print("   {0}  |  {1}  |  {2}   ".format(printable_state.grid[1][0], printable_state.grid[1][1],
                                                 printable_state.grid[1][2]))
        print("-------------------")
        print("   {0}  |  {1}  |  {2}   ".format(printable_state.grid[2][0], printable_state.grid[2][1],
                                                 printable_state.grid[2][2]))
        print()

    def get_empty_cells(self):
        empty_cells = []
        for row in range(0, 3):
            for cell in range(0, 3):
                if self.grid[row][cell] is None:
                    empty_cells.append((row, cell))
        return empty_cells

    def get_copy(self):
        copy = gamestate()
        for row in range(0, 3):
            for cell in range(0, 3):
                copy.grid[row][cell] = self.grid[row][cell]
        return copy

import gamestate

class gamestate_tree_node:
    def __init__(self, gamestate, current_player, decision):
        self.gamestate = gamestate
        self.current_player = current_player
        self.decision = decision
        self.child_nodes = self.calculate_child_nodes()

        if len(self.child_nodes) != 0:
            self.o_wins = self.calculate_o_wins()
            self.x_wins = self.calculate_x_wins()
            self.draws = self.calculate_draws()
        else:
            self.o_wins = 0
            self.x_wins = 0
            self.draws = 0
            result = self.gamestate.check_winner()
            if result == "O":
                self.o_wins = 1
            elif result == "X":
                self.x_wins = 1
            else:
                self.draws = 1

    def calculate_child_nodes(self):
        new_child_nodes = []
        if not self.gamestate.is_done():
            empty_cells = self.gamestate.get_empty_cells()
            for empty_cell in empty_cells:
                future_gamestate = self.gamestate.get_copy()
                future_gamestate.grid[empty_cell[0]][empty_cell[1]] = self.current_player

                # Player Swap
                if self.current_player == "O":
                    next_player = "X"
                else:
                    next_player = "O"

                new_child_nodes.append(gamestate_tree_node(future_gamestate, next_player, empty_cell))
        return new_child_nodes

    def calculate_o_wins(self):
        o_wins = 0
        for child in self.child_nodes:
            o_wins += child.o_wins
        return o_wins

    def calculate_x_wins(self):
        x_wins = 0
        for child in self.child_nodes:
            x_wins += child.x_wins
        return x_wins

    def calculate_draws(self):
        draws = 0
        for child in self.child_nodes:
            draws += child.draws
        return draws

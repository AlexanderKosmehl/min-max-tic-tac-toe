from gamestate import gamestate
from gamestate_tree_node import gamestate_tree_node

# Main
initial_gamestate = gamestate()
current_player = "O"
print("Welcome to Tic Tac Toe!")
# print("Available modes: 1 - Player vs Player | 2 - Player vs Computer | 3 - Tree Mode")
# gamemode = int(input("Choose a mode:"))
#
# # Player vs Player
# if gamemode == 1:
#     while current_gamestate.is_done() == False:
#         current_gamestate.print_gamestate()
#         while(True):
#             choice = [int(x) for x in input("Pick a cell: ").split(" ")]
#             if current_gamestate.grid[choice[0]][choice[1]] is None:
#                 current_gamestate.grid[choice[0]][choice[1]] = current_player
#                 break
#             else:
#                 print("That cell is not empty!")
#         # Player Swap
#         if current_player == "O":
#             current_player = "X"
#         else:
#             current_player = "O"
#
#     current_gamestate.print_gamestate()
#     winner = current_gamestate.check_winner()
#     if winner != 0:
#         print(winner + " wins!")
#     else:
#         print("Draw!")

# Calculate state tree
state_tree_root = gamestate_tree_node(initial_gamestate, current_player, None)
current_tree_node = state_tree_root
current_gamestate = initial_gamestate.get_copy()

while not current_gamestate.is_done():

    # Player Turn
    current_gamestate.print_gamestate()
    while(True):
        choice = [int(x) for x in input("Pick a cell: ").split(" ")]
        if current_gamestate.grid[choice[0]][choice[1]] is None:
            current_gamestate.grid[choice[0]][choice[1]] = current_player
            break
        else:
            print("That cell is not empty!")

    # Computer Turn
    if not current_gamestate.is_done():
        for child_node in current_tree_node.child_nodes:
            if child_node.decision == (choice[0], choice[1]):
                current_tree_node = child_node
                break

        current_tree_node.child_nodes.sort(key=lambda child: child.o_wins)
        current_gamestate.grid[current_tree_node.child_nodes[0].decision[0]][current_tree_node.child_nodes[0].decision[1]] = "X"


current_gamestate.print_gamestate()
winner = current_gamestate.check_winner()
if winner != 0:
    print(winner + " wins!")
else:
    print("Draw!")


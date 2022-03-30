from copy import deepcopy
from Sudoku_Board import SB, Invalid_Board


class Solution:
    def solveSudoku(self, board) -> None:
        try:
            start_sb = SB(board)
        except Invalid_Board:
            print('Initial board not valid')
            return
        final_sb = self.dfs(start_sb)
        if final_sb is None:
            print('No solution found')
            return
        final_sb.print_b()
        for loc, entry in final_sb.board_dict.items():
            board[loc[0]][loc[1]] = entry.value

    def dfs(self, start_sb: SB):
        queue = [start_sb]
        solved = False
        while not solved and len(queue) != 0:
            state = queue.pop(0)
            if state.check_solved():
                solved = True
                return state
            else:
                expand_loc = state.get_llp()
                possibles = state.loc_get_range(expand_loc)
                for value in possibles:
                    child_state = deepcopy(state)
                    if child_state.loc_set_val(expand_loc, value):
                        queue = [child_state] + queue
        return None

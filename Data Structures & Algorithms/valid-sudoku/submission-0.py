class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_to_set = defaultdict(set)
        row_to_set = defaultdict(set)
        subbox_to_set = defaultdict(set)

        for row in range(9):
            for col in range(9):
                curr_val = board[row][col]
                if curr_val == '.':
                    continue 

                if curr_val in col_to_set[col] or curr_val in row_to_set[row] or curr_val in subbox_to_set[(col // 3, row // 3)]:
                    return False
                
                col_to_set[col].add(curr_val)
                row_to_set[row].add(curr_val)
                subbox_to_set[(col // 3, row // 3)].add(curr_val)
        
        return True

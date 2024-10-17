class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]  # Set for each row
        cols = [set() for _ in range(9)]  # Set for each column
        boxes = [set() for _ in range(9)] # Set for each 3x3 sub-box
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                
                if num == '.':  # Skip empty cells
                    continue
                
                # Check the row
                if num in rows[i]:
                    return False
                rows[i].add(num)
                
                # Check the column
                if num in cols[j]:
                    return False
                cols[j].add(num)
                
                # Check the 3x3 sub-box
                box_index = (i // 3) * 3 + (j // 3)  # Box index calculation
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)
        
        return True

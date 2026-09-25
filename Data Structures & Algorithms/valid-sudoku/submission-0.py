class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # since the board length is max 9, isn't brute force a valid solution here?
        # literally do a hashmap dupe check for all row column subboxes
        for row in board:
            seen = set()
            for num in row:
                if num == ".":
                    continue

                if num in seen:

                    return False
                else: # num not in seen:
                    seen.add(num)
        for col in range(9):
            seen = set()
            for i in range(9):
                num = board[i][col]
                if num == ".":
                    continue

                if num in seen:
                    print("columns")
                    return False
                else: # num not in seen:
                    seen.add(num)
        for i in range(3):
            seen = set()
            for j in range(3):
                seen.clear()
                for m in range(3):
                    for n in range(3):
                        k = 3 * i + m
                        l = 3 * j + n
                        num = board[k][l]
                        if num == ".":
                            continue

                        if num in seen:
                            print(f"3x3s, iteration {i} {j} {k} {l}")
                            return False
                        else: # num not in seen:
                            seen.add(num)
                seen.clear()
    
        return True

        
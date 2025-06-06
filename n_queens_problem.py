
class Solution:
    def solveNQueens(self, n:int)-> list[list[str]]:
        col = set()
        posDiag = set()    #(r+c)
        negDiag = set()    #(r-c)
        
        sol = 0
        res = []
        board = [['.']*n for i in range(n)]

        def backTrack(r):
            if r == n:
                nonlocal sol
                copy = ["".join(row) for row in board]
                res.append(copy)
                sol+= 1
                return

            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = 'Q'

                backTrack(r+1)

                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = '.'

        backTrack(0)
        return (res, sol)

if __name__== "__main__":
    s = Solution()
    (res, sol) = s.solveNQueens(5)
    print("There are {} solutions for this problem".format(sol))
    print(res)


            

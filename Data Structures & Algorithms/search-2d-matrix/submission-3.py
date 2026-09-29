class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lenl = len(matrix)
        lenr = len(matrix[0])
        l = 0
        r = lenl*lenr-1
        res = False
        if matrix[l][l] == target or matrix[lenl-1][lenr-1] == target:
            res = True
        while r>l+1:
            n = (r+l)//2
            if target > matrix[(n//lenr)][n%lenr]:
                l = n
            elif target < matrix[(n//lenr)][n%lenr]:
                r = n
            else:
                res = True
                break
        return res
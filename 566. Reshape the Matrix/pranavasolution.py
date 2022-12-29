class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if (r*c) != (len(mat) * len(mat[0])):
            return mat
        
        res = []
        temp = []
        count = 0

        for row in mat:
            for num in row:        
                temp.append(num)
                count += 1
                if count >= c:
                    count = 0
                    res.append(temp)
                    temp = []
        return res

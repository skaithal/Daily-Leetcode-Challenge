
#  O(n) Runtime & O(n) Space
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # base cases - R: O(1), M: O(1)
        m, n = len(mat), len(mat[0])
        if not mat or (m * n) != (r * c):
            return mat

        # create new empty matrix, list - R: O(1), M: O(1)
        new_mat = []
        num_list = []

        # run through curr matrix, save the items numerically - R: O(n), M: O(n)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                num_list.append(mat[i][j])
        
        # fill in new empty matrix - R: O(n), M: O(n)
        for _ in range(r):
            row = []
            for _ in range(c):
                item = num_list.pop(0)
                row.append(item)
            new_mat.append(row)
        
        return new_mat


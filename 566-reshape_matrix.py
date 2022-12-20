"""
566. Reshape the Matrix
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
"""


# My Solution, O(n) Runtime & O(n) Space
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


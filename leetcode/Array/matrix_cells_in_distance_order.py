''' PROBLEM - Matrix Cells in Distance Order
You are given four integers row, cols, rCenter, and cCenter. There is a rows x cols matrix and you are on the cell with the coordinates (rCenter, cCenter).

Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter) from the smallest distance to the largest distance. 
You may return the answer in any order that satisfies this condition.

The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.
'''


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:
        a=[]
        a1=[]
        a3=[]
        for i in range(rows):
            for j in range(cols):
                a.append([i,j])
                a1.append(abs(i-rCenter)+abs(j-cCenter))
        for i in range(len(list(set(a1)))):
            for j in range(rows*cols):
                if i==a1[j]  :
                    a3.append(a[j])
        return a3
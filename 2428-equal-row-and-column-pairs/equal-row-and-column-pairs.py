class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Brute force
        # reading each list will be a row
        # How to form the columns? loop? Anything native in python?
        # compare lists? will ne n*n very expensive.
        # tuple(list) are hashable
        
        pairs = 0
        rows = Counter(tuple(x) for x in grid)

        for i in range(len(grid)):
            c = []
            for j in range(len(grid)):
                c.append(grid[j][i])
            pairs = pairs + rows[tuple(c)]

        return pairs
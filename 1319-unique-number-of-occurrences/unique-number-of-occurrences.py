class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)

        counts_values = counts.values()

        if len(set(counts_values)) == len(counts_values):
            return True
        else:
            return False
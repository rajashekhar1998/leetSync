class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)

        counts = counts.values()

        if len(set(counts)) == len(counts):
            return True
        else:
            return False
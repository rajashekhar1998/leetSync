class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # relative heights wrt the starting height

        relative_altitude = 0
        max_altitude = 0

        for change in range(len(gain)):
            relative_altitude = relative_altitude + gain[change]
            max_altitude = max(max_altitude, relative_altitude)

        return max_altitude
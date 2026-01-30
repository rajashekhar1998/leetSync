class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack implementation and iteration checking exlosion rules
        stack = []

        for item in asteroids:

            while stack and stack[-1] > 0 and item < 0:
                diff = stack[-1] + item
                
                if diff < 0:
                    stack.pop()
                    continue
                elif diff == 0:
                    stack.pop()
                    item = 0
                    break
                elif diff > 0:
                    item = 0
                    break

            if item!=0:
                stack.append(item)
                
        return stack
from typing import List

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        ans = 0

        for x in range(201):
            for y in range(201):
                for cx, cy, r in circles:
                    if (x - cx) ** 2 + (y - cy) ** 2 <= r * r:
                        ans += 1
                        break

        return ans
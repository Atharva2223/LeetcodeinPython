from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # I initialize the left boundary of the sliding window.
        left = 0

        # I keep track of how many zeros are currently inside the window.
        zero_count = 0

        # I store the maximum valid window length found so far.
        max_length = 0

        # I move the right boundary from the start to the end of the array.
        for right in range(len(nums)):

            # If the new element entering the window is 0, I need one flip for it.
            if nums[right] == 0:

                # I increase the zero count for the current window.
                zero_count += 1

            # While the window has more than k zeros, it is invalid.
            if zero_count > k:

                # If the element leaving from the left is 0, I remove one zero from the window.
                if nums[left] == 0:

                    # I decrease the zero count because this zero is no longer inside the window.
                    zero_count -= 1

                # I move the left boundary forward to shrink the window.
                left += 1

            # At this point, the window from left to right has at most k zeros.
            current_length = right - left + 1

            # I update the maximum length if the current valid window is longer.
            max_length = max(max_length, current_length)

        # I return the maximum number of consecutive ones possible after at most k flips.
        return max_length
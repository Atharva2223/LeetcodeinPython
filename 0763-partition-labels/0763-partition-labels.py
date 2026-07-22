from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Hashmap storing the last occurrence of each character
        last_position = {}

        for index, character in enumerate(s):
            last_position[character] = index

        partitions = []

        partition_start = 0
        partition_end = 0

        for index, character in enumerate(s):
            # Expand the current partition if this character
            # appears farther in the string
            partition_end = max(
                partition_end,
                last_position[character]
            )

            # Current partition is complete
            if index == partition_end:
                partition_size = partition_end - partition_start + 1
                partitions.append(partition_size)

                # Start the next partition
                partition_start = index + 1

        return partitions
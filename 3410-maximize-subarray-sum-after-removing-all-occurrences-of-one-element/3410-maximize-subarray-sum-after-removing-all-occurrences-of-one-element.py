from typing import List
from collections import defaultdict


class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        NEG_INF = float("-inf")

        def make_node(value):
            return [value, value, value, value]

        def deleted_node():
            return [0, NEG_INF, NEG_INF, NEG_INF]

        def merge(left, right):
            total = left[0] + right[0]
            prefix = max(left[1], left[0] + right[1])
            suffix = max(right[2], right[0] + left[2])
            best = max(left[3], right[3], left[2] + right[1])

            return [total, prefix, suffix, best]

        tree = [[0, NEG_INF, NEG_INF, NEG_INF] for _ in range(4 * n)]

        def build(node, start, end):
            if start == end:
                tree[node] = make_node(nums[start])
                return

            mid = (start + end) // 2

            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)

            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        def update(node, start, end, index, new_node):
            if start == end:
                tree[node] = new_node
                return

            mid = (start + end) // 2

            if index <= mid:
                update(2 * node, start, mid, index, new_node)
            else:
                update(2 * node + 1, mid + 1, end, index, new_node)

            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        build(1, 0, n - 1)

        answer = tree[1][3]
        positions = defaultdict(list)

        for i, num in enumerate(nums):
            if num < 0:
                positions[num].append(i)

        for value, indexes in positions.items():
            for index in indexes:
                update(1, 0, n - 1, index, deleted_node())

            if tree[1][3] != NEG_INF:
                answer = max(answer, tree[1][3])

            for index in indexes:
                update(1, 0, n - 1, index, make_node(value))

        return answer
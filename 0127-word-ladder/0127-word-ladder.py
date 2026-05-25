from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 1. Put all allowed words into a set for O(1) lookups.
        wordSet = set(wordList)
        # If endWord isn't in the list, we can never reach it.
        if endWord not in wordSet:
            return 0

        # 2. Initialize BFS queue with (beginWord, stepCount=1).
        queue = deque()
        queue.append((beginWord, 1))

        # 3. Standard BFS loop
        while queue:
            curr_word, level = queue.popleft()
            # If we've reached the end, return the number of steps.
            if curr_word == endWord:
                return level

            # 4. Try changing each letter in curr_word
            for i in range(len(curr_word)):
                # For each position, try all possible lowercase letters
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    # Skip if the letter is the same
                    if ch == curr_word[i]:
                        continue
                    # Form a new word by replacing the i-th letter
                    new_word = curr_word[:i] + ch + curr_word[i+1:]
                    # If the new word is in our set, it's a valid step
                    if new_word in wordSet:
                        # Add it to the queue with stepCount + 1
                        queue.append((new_word, level + 1))
                        # Remove from set so we don't visit again
                        wordSet.remove(new_word)

        # If queue empties without finding endWord, there's no path
        return 0
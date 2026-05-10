class Solution:
    def isValid(self, s: str) -> bool:
        # Early exit: odd length can't be balanced
        if len(s) & 1:
            return False

        stack = []
        expect = {'(' : ')', '[' : ']', '{' : '}'}

        for ch in s:
            if ch in expect:                 # opening -> push the expected closer
                stack.append(expect[ch])
            else:                             # closing -> must match top
                if not stack or stack.pop() != ch:
                    return False

        return not stack

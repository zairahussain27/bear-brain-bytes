class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        stack = []

        for char in s:
            if char in brackets:
                stack.append(char)  # if it opens, save it
            else:
                if stack and brackets[stack[-1]] == char:  # if last saved bracket matches this one
                    stack.pop()  # remove it because the pair is complete
                else:
                    return False  # wrong closing bracket or nothing to close

        return len(stack) == 0  # nothing should be left open
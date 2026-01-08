class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = { ')':'(', ']':'[','}':'{'}

        for cha in s:
            if cha in match:
                if stack and stack[-1]==match[cha]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(cha)
        return True if not stack else False

        
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == "[" or char == "(" or char == "{":
                stack.append(char)
            else: # closing parenthesis
                if not stack:
                    return False
                compare = stack.pop()
                if char == ")" and compare != "(":
                    return False
                elif char == "]" and compare != "[":
                    return False
                elif char == "}" and compare != "{":
                    return False

        return not stack

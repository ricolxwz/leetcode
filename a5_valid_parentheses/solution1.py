class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for index, value in enumerate(s):
            if (value == "(" or value == "[" or value == "{"):
                if index == len(s) - 1:
                    return False
                else:
                    stack.append(value)
            else:
                if len(stack) == 0 or value == ")" and stack[-1] != "(" or value == "]" and stack[-1] != "[" or value == "}" and stack[-1] != "{":
                    return False
                else:
                    stack.pop(-1)
        if len(stack) != 0:
            return False
        return True

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if (tok == '+'):
                stack.append(stack.pop() + stack.pop())
            elif (tok == '-'):
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 - op1)
            elif (tok == '*'):
                stack.append(stack.pop() * stack.pop())
            elif (tok == '/'):
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(op2 / op1))
            else:
                stack.append(int(tok))
        return stack[0]
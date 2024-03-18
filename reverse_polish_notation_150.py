class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res=0
        for i in tokens:
            match(i):
                case '+':
                    op2=int(stack.pop())
                    op1=int(stack.pop())
                    res=op2+op1
                    stack.append(str(res))
                case '-':
                    op2=int(stack.pop())
                    op1=int(stack.pop())
                    res=op1-op2
                    stack.append(str(res))
                case '*':
                    op2=int(stack.pop())
                    op1=int(stack.pop())
                    res=op1*op2
                    stack.append(str(res))
                case '/':
                    op2=int(stack.pop())
                    op1=int(stack.pop())
                    res=int(op1/op2)
                    stack.append(str(res))
                case _:
                    stack.append(i)
        return int(stack.pop())
                

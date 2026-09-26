class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+": lambda a,b: a+b,
            "-": lambda a,b: a-b,
            "*": lambda a,b: a*b,
            "/": lambda a,b: int(a/b)}
        dct = []
        for i in tokens:
            if i not in ops:
                dct.append(int(i))
            else:
                res = ops[i](dct[-2], dct[-1])
                dct.pop()
                dct.pop()
                dct.append(res)
        return dct[-1]
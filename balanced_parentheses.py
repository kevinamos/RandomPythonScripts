class BalancedParentheses():
    def __init__(self, s):
        self.s=s
    def IsBalanced(self):
        if len(self.s)%2!=0:
            return False
        stack=[]
        opening="(,{,["
        d={'(':')', '{':'}', '[':']'}
        for paren in self.s:
            if paren in opening:
                stack.append(paren)
            else:
                if len(stack)<1:
                    return False
                last_opening_paran=stack.pop()
                if d[last_opening_paran]!=paren:
                    return False
        return len(stack)==0
        

b=BalancedParentheses('')
print(b.IsBalanced())

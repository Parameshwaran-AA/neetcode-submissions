class Solution:
    def isValid(self, s: str) -> bool:
        # we will have a Stack
        stack = []

        # we need to append the stack with the opener and check the closer 
        for char in s:
            
            # Here we handle the opener and stack them appropriately 
            if(char in ['(', '{', '[']):
                stack.append(char)
            
            else:
                if not stack or not  ( (stack[-1] == '(' and char ==')')  or ( stack[-1] == '[' and char == ']')  or (stack[-1] == '{' and char == '}' )) :
                    return False    
                stack.pop()

        
        return len(stack) == 0
            
        
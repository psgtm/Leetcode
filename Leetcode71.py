class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the path by "/" and use a stack for simplification
        stack = []
        components = path.split('/')
        
        for component in components:
            if component == '..':
                if stack:  # Pop only if the stack is not empty
                    stack.pop()
            elif component and component != '.':  # Ignore empty strings and "."
                stack.append(component)
        
        # Join the stack to form the simplified path
        return '/' + '/'.join(stack)

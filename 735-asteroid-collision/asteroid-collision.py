class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            while stack and stack[-1] > 0 and ast<0:
                if stack[-1] < -ast:
                    stack.pop()
                elif stack[-1] == -ast:
                    stack.pop()
                    ast = 0
                else:
                    ast = 0
            if ast!= 0:
                stack.append(ast)
        return stack

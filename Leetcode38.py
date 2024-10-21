class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        
        for _ in range(n - 1):
            current = result
            result = ""
            count = 1
            
            for i in range(1, len(current)):
                if current[i] == current[i - 1]:
                    count += 1
                else:
                    result += str(count) + current[i - 1]
                    count = 1
            
            result += str(count) + current[-1]
        
        return result

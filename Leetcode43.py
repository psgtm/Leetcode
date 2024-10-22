class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize an array to store the result
        result = [0] * (len(num1) + len(num2))
        
        # Reverse both numbers to make multiplication easier
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        # Multiply each digit and add the results
        for i in range(len(num1)):
            for j in range(len(num2)):
                mul = int(num1[i]) * int(num2[j])
                result[i + j] += mul
                # Carry over
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
        
        # Skip leading zeros in the result
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        # Reverse the result and convert to string
        return ''.join(map(str, result[::-1]))

# Example usage:
sol = Solution()
print(sol.multiply("123", "456"))  # Output: "56088"

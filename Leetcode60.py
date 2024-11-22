class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial

        # Create a list of numbers to pick from
        numbers = list(range(1, n + 1))
        # Adjust k to zero-based indexing
        k -= 1
        # Build the permutation
        result = []

        for i in range(n):
            # Calculate the index of the current number
            fact = factorial(n - 1 - i)
            index = k // fact
            result.append(str(numbers.pop(index)))
            # Update k
            k %= fact

        return ''.join(result)

class Solution:
    def intToRoman(self, num: int) -> str:
        # List of tuples containing the Roman numeral and its corresponding integer value
        val = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        
        roman_numeral = ""
        
        # Iterate over the value-roman pairs
        for (value, symbol) in val:
            # While num is greater than or equal to the value
            while num >= value:
                roman_numeral += symbol  # Add the corresponding roman numeral to the result
                num -= value  # Subtract the value from num
                
        return roman_numeral

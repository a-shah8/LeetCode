## Create 2 arrays values and roman

class Solution:
    def intToRoman(self, num: int) -> str:
        
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        
        result = ''

        for i, numb in enumerate(values):
            while num>=numb:
                result += roman[i]
                num -= numb
            if num==0:
                return result

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1, -1, -1):
            
            # Add 1 to current digit
            if (digits[i]+1) <= 9:  # if new digit <= 9
                digits[i] += 1      # perform addition
                return digits       # and return
            
            # If new digit > 9
            digits[i] = 0           # make current digit 0
            
            # If all trailing digits are 0
            if i==0:
                digits.insert(0,1)  # insert 1 at position 0
        
        return digits

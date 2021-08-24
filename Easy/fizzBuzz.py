class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        answer = []
        
        fizz_buzz_dict = {3: "Fizz", 5: "Buzz"}
        
        for num in range(1, n+1):
            
            string = ''
            for key in fizz_buzz_dict.keys():
                
                if num % key == 0:
                    string += fizz_buzz_dict[key]
                    
            if string=='':
                string = str(num)
                
            answer.append(string)
            
        return answer

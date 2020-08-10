class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        try:
            finalList = []
            for i in range(1, n+1):
                if i % 3 == 0 and i % 5 == 0:
                    finalList.append("FizzBuzz")
                elif i % 3 == 0:
                    finalList.append("Fizz")
                elif i % 5 == 0:
                    finalList.append("Buzz")
                else:
                    finalList.append(str(i))
            return(finalList)
        except:
            return None

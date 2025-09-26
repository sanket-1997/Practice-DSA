class Solution:
    @staticmethod
    def printNumbers(number):
        if number < 1:
            return
        
        print(number)
        Solution.printNumbers(number -1)

Solution.printNumbers(10)
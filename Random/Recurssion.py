class Solution:
    @staticmethod
    def printNumbers(number):
        if number < 1:
            return
        
        print(number)
        Solution.printNumbers(number -1)

Solution.printNumbers(10)




n =3
s = list(range(2,5))
print(s)
print(n in range(2,5))
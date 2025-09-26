class Solution:
    def print_number( self, i, n):
        if i>n:
            return
        print(i)
        self.print_number(i+1,n)


#main function to run the code


s = Solution()
s.print_number(1, 10)


#TimeComplexity = O(N)
#Space Complexity = O(N)
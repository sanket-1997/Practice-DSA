class Solution:
    def print_numbers(self, i, n):
        if i< n:
            return
        print(i)

        self.print_numbers(i-1, n)


s = Solution()
s.print_numbers(10, 1)



#Time Complexity = O(N)
#Space Complexity = O(N)



class Solution:
    def sum_n_number(self, n):
        if n ==0:
            return 0
        
        return n + self.sum_n_number(n-1)
    


s = Solution()
print(s.sum_n_number(3))



#Time Complexity = O(N)
#Space Complexity = O(N)


s = [10, 20, 30, 50]
print(s[::-1])
class Solution:
    def reverse_an_array(self, i: int, arr: list, n: int):
        if i >= n // 2:
            return
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
        self.reverse_an_array(i+1, arr, n)

arr = [x for x in range(10)]
s = Solution()
s.reverse_an_array(0, arr, 10)  # modifies arr in place
print(arr)                      # [9,8,7,6,5,4,3,2,1,0]

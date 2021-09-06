class Solution:
    def climbStairs(self, n: int) -> int:
        a = [1, 2]
        if len(a) >= n:
            return a[n - 1]
        else:
            while len(a) < n:
                a.append(a[len(a) - 1] + a[len(a) - 2])
            return a[len(a) - 1]

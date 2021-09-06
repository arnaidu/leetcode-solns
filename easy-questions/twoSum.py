from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = dict()
        for i in range(len(nums)):
            first_number = nums[i]  # first number in the sum 
            next_number = target - first_number  # the next number we would need for sum
            if ans.get(next_number) is not None:
                return [i, ans[next_number]]
            else:
                ans[first_number] = i

if __name__ == "__main__":
    soln = Solution()
    nums = [2, 5, 7, 11]
    target = 9
    expected = [0, 2]
    output = soln.twoSum(nums, target)
    assert(expected == sorted(output))

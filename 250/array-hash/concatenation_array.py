"""
You are given an integer array nums of length n. 
    Create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
    Specifically, ans is the concatenation of two nums arrays.
        nums = [1,2,3,4] n = 4
        nums[0] = 1
        ans[0] = 1
        ans = [1,2,3,4]

        ans[0+4] = nums[0]
        ans[4] = 1

Return the array ans.

Example 1: Input: nums = [1,4,1,2] Output: [1,4,1,2,1,4,1,2]

Example 2: Input: nums = [22,21,20,1] Output: [22,21,20,1,22,21,20,1]

constraints: size of array, how big the nums can get

"""

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums) * 2

        for i in range(len(ans)):
            if i < len(nums):
                ans[i] = nums[i]
            else:
                ans[i] = nums[i - len(nums)]
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.getConcatenation([22,21,20,1]))
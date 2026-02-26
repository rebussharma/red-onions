"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
constrainsts: size of array
"""

class Solution:
    def hasDeplicate(self, nums:list[int]) -> bool:
        s = set()

        for num in nums:
            s.add(num)

        return len(s) != len(nums)
    # return len(set(nums)) != len(nums)
    
if __name__ == "__main__":
    s = Solution()
    print(s.hasDeplicate([1,2,3]))

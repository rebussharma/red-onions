"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: nums = [3,4,5,6], target = 7 Output: [0,1]

Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
Input: nums = [4,5,6], target = 10 Output: [0,2]

Example 3: Input: nums = [5,5], target = 10 Output: [0,1]

constrains: length of array, number size, negative positive numbers

Quesiton: you want two indices, but what if array size is 1?

"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
            Input: nums = [3,4,5,6], target = 7 Output: [0,1]

            1. double iteration => all possible pair => sure shot answer
                Brute Force, hight TC
            
            2. I create a hashmap: with nums as keys and their index as value
                I get 3, if differece of target - 3 = 4 is in hasmap
                    I return index of 3 and index of 4
                Since 3 is first elment, hashMap is empty here so we cannot find target - 3
                we add 3 into hasmap

            
        """
        if len(nums) < 2:
            return
        res = {}
        
        for i in range(len(nums)):
            if target - nums[i] in res:
                return [res.get((target - nums[i])), i]
            res[nums[i]] = i

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([5,5], 10))
        
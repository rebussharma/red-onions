"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times in the array. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [5,5,1,1,1,5,5]

Output: 5

Example 2:

Input: nums = [2,2,2]

Output: 2

constraints:
size of array, number range
"""
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        '''
            5,5,1,1,1,5,5

            i      cnt      m
            5       1       5
            5       2       5
            1       1       5
            1       2       5
            1       3       1
            5       3       1
            5       4       5

            1. I cannot reset count to 0 
            2. I need to keep track of frequency of each element in the array

            If I need freq of each elment then i need a key value DS: hashamp       
        '''
        res = defaultdict(list)
        max_val = 0
        for n in nums:
            res[n] = res.get(n, 0) + 1
            if res.get(n) > max_val:
                max_val = n
        return max_val if max_val > len(nums)/2 else -1

        # max_key = max(res)
        # print(max_key, res)
        # return max_key if res.get(max_key) > len(nums)/2 else None

if __name__ == "__main__":
    s = Solution()
    s.majorityElement([3,3,4])
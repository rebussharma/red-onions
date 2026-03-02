"""
Given an array of strings strs, group all anagrams together into sublists. 
You may return the output in any order.
Example 1: Input: strs = ["act","pots","tops","cat","stop","hat"]   Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2: Input: strs = ["x"] Output: [["x"]]

Example 3: Input: strs = [""] Output: [[""]]

constraints: 
    1. strings: case? 
    2. array: length of array
"""
from collections import defaultdict

class Solution:

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) < 2:
            return[[strs]]
        res = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            res[key].append(s)
        return list(res.values())
    
    def groupAnagramsBetter(self, strs: list[str]) -> list[list[str]]:
        if len(strs) < 2:
            return[[strs]]
        '''
            Take for example two strings 'knee' and 'keen'
                Both have 1k, 1n and 2e
                so what we can do is create a hastable
                    hashtable where 1k, 1n, 2e will be the KEY and knee and keen will be appended as values
                But how to get 1k 1n 2e from both 'knee' and 'keen'
                    we used ordinals
            So basically
                1. loop through each word
                2. get its ord value
                3. add ord value as key and word as value
        '''
        res = defaultdict(list)
        for s in strs: # 1. loop though each word
            count = [0] * 26 # 2. get each words ordinal value
            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s) # 3. add the ord value as key and word as value

        return list(res.values())

if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagramsBetter(["act","pots","tops","cat","stop","hat"]))
        
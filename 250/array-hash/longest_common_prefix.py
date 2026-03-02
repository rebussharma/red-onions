"""
You are given an array of strings strs. Return the longest common prefix of all the strings.

If there is no longest common prefix, return an empty string "".

Example 1: Input: strs = ["bat","bag","bank","band"] Output: "ba"
Example 2: Input: strs = ["bat","dat"] Output: ""

"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        first = strs[0]
        res = ""
        '''
            Common prefix means prefix MUST be a part of first word in array.
                So, take the first words and do the comparison
            if first letter of FIRST word is also the first letter of EACH element in array, add that letter to result
                if second letter of FIRST word is also the second letter of EACH element in array, add that letter to result
           But what if one of the words is an empty string or a shorter string (i.e got, go), 
            first word is got, we check if g is in second word (go), the check if o in go then check if t in go (index out of bout issue). 
            So, to make sure we don't encounter this issue its best to make sure we're first making sure the index we're checking 2(index of t in got) 
                is smaller than length of second word(go); if not we return result up to that point
        '''
        for i, letter in enumerate(first):
            for word in strs[1:]:
                if word[i] != letter or i >= len(word): # word[i] != letter, meaning the 2nd words letter at index of first word's letter is not same
                    return res
            res += letter

        return res
                
if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["abc", "zab"]))
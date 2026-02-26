"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
Input: s = "racecar", t = "carrace"
Input: s = "jar", t = "jam"

question: exact same number of chars or just exact chars?
    i.e is bob and boo anagram?
answer: no, anagram means same NUMBER of chars too

constrains: dealing with letters. So, case sensitivuty
""" 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            anagram means 2 strings with same num/type of chars
            1. make sure each chars in 's' is also in 't'
                we could loop through using 2 loops and check if each char in 's' is in 't't
                    but 2nd 'c' raceCar will match to first c in Carrace isntead of last c carraCe. 
                    so, this won't work
            2. create a hashset with key value pair for BOTH s and t
                key being chars, value being thier frequency in string
                if both hashsets are equal then we're good
                2a. creating 1st hashSet is On, 2nd hashset is alsop On
                TC: 2On = On
        """
        if len(s) != len(t):
            return False    
        s_set = {}
        t_set = {}
        for i in s:
            s_set[i] = s_set.get(i, 0) +  1
        for j in t:
            t_set[j] = t_set.get(j, 0) +  1
        return s_set == t_set


if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("jama", "maja"))
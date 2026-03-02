"""
You are given an integer array nums and an integer val. Your task is to remove all occurrences of val from nums in-place.

After removing all occurrences of val, return the number of remaining elements, say k, such that the first k elements of nums do not contain val.

Note:

    The order of the elements which are not equal to val does not matter.
    It is not necessary to consider elements beyond the first k positions of the array.
    To be accepted, the first k elements of nums must contain only elements not equal to val.

Return k as the final result.

Example 1:

Input: nums = [1,1,2,3,4], val = 1

Output: [2,3,4]

Explanation: You should return k = 3 as we have 3 elements which are not equal to val = 1.

Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2

Output: [0,1,3,0,4]

Explanation: You should return k = 5 as we have 5 elements which are not equal to val = 2.

YOu cannot create another array for any reason
"""
class Solution:
    '''
        THIS WAS A TRICKY ONE.
        I HAD 3 WRONG IDEA AND 1 CORRECT IDEA
        Basically, we can NOT create another array, that will eat up more space.
        1. [WRONG IDEA] Basic thought was to just iterate over the array, compare how many elements are equal to val and return that count.
            This is NOT enough as the question asks us to remove element IN PLACE
        2. [WRONG IDEA] We could also find which element is equal to val and do nums.remove()
            But this will also no work as On2 and doesnt really remove in place

        At this time I was out of thoughts, but after examining both example arrays closely,
            it was clear that I just need to shift elements NOT EQUAL to val to the left.
            nums = [1,1,2,3,4]         val = 1     OUTPUT = [2,3,4,_,_]
            nums = [0,1,2,2,3,0,4,2]   val = 2     OUTPUT: [0,1,3,0,4,_,_,_]

        3. [WRONG IDEA] Now I thought if I compare each element in array to val,
            whenever I find element == val, I can assign the index of that element to another variable, say k.
            Then set item at index k to the next element that is not val.
            If next element is also equal to val then update k to the index of that element,
                Then set nums[k] to next element that is not val
                Basically:
                for array [1, 1, 2, 3, 4], lets set k at 0 to start with

                n    val    k (index)     notes
                1     1     0             since n == val, we set k to the index of n, do nothing else
                1     1     1             since n == val, we update k to index of n, d nothig else
                2     1     1             since n != val, we leave k as is, update nums array so that nums[k] = 
                                            This way we do shift the array to right BUT THIS IS NOT CORRECT
                                            AS WE SHIFT ARRAY ONLY SPACE TO RIGHT. CURRENTLY ARRAY LOOKS LIKE [1,2...]
        4. [RIGHT IDEA]
            At this time I was sure I need to do two things
                1. shift array elements to left
                2. NOT update array when 'val' equals array element
            I wanted to check if there was a way I could shift array when element is NOT equal to 'val'

            So, what I'd do is that create a variable k, so that I can safely re-assign array elements
            Update the value of K when array elements != 'val'
            
            Loop through the array,
                if item != val
                    set nums[k] = item (no change in many cases)
                    now that k index is already used to assign it to item, move the index
                    k += 1
                if item == val
                    do nothing, so that k (index) is still pointing to the number where item != val
            
            for array [0,1,2,2,3,0,4,2], lets set k at 0 to start with

            n (nums ) v(val)     result nums
            0            2         0, ...... [no chnage]
            1            2         0, 1, ...... [no chnage]
            2            2         0, 1, ...... [chnage. we want to NOT INCLUDE 2]
            2            2         0, 1, ...... [chnage. we want to NOT INCLUDE 2] 
            3            2         0, 1, 3 ..... [change, we moved '3' to the position AFTER 0,1]
            0            2         0, 1, 3 ..... [change, we moved '0' to the position AFTER 0,1, 3]
                IT's important to think that we moved numbers to position AFTER other elemnets.
                Not think as if we SWAPPED postion with '2' or elements that == val 




    '''
    def removeElement(self, nums: list[int], val: int) -> int:
        count = 0
        res = []
        for i, n in enumerate(nums):
            if n != val:
                count += 1
                res.append(n)
        return count, res

if __name__ == "__main__":  
    s = Solution()
    print(s.removeElement([0,1,2,2,3,0,4,2], 2))
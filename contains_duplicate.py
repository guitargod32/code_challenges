class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
        """
        h = {}
        
        for num in nums:
            if h.has_key(num): #find any duplicate, we return true
                return 'true'
            else:
                h[num] = num #add to dictionary


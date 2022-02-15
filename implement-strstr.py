class Solution(object):
    """Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack."""
    def strStr(self, haystack, needle):
        return haystack.find(needle) if needle in haystack else -1 if needle else 0
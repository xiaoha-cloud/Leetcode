class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort the array and use a set to record the element
        # O(n)
        # O(n)

        s = set(nums)
        longest = 0

        for num in s:
            if num-1 not in s:
                next_num=num+1
                length =1
                while next_num in s:
                    length +=1
                    next_num +=1
                longest = max(longest, length)
        return longest

        
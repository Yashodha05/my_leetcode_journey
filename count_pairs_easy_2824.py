#2824. Count Pairs Whose Sum is Less than Target
#Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        count=0
        while(i<j):
            sum=nums[i]+nums[j]
            if (sum<target):
                count=count+(j-i)
                i=i+1
            else:
                j=j-1

        return count

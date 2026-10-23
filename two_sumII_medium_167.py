#167. Two Sum II - Input Array Is Sorted
#You are given a 1-indexed array of integers numbers that is already sorted in non-decreasing order.

#Find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i=0
        j=len(numbers)-1
        while(i<j):
            sum=numbers[i]+numbers[j]
            if (sum>target):
                j=j-1
            elif sum<target:
                i=i+1
            else:
                return[i+1, j+1]
        return []

#75. Sort Colors
#You are given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

#You must solve this problem without using the library's sort function.

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        k=0
        j=len(nums)-1

        while(k<=j):
            if(nums[k]==0):
                temp=nums[k]
                nums[k]=nums[i]
                nums[i]=temp

                i=i+1
                k=k+1
            elif(nums[k]==1):
                k=k+1
            else:
                temp=nums[k]
                nums[k]=nums[j]
                nums[j]=temp

                j=j-1

class Solution(object):
    def sortedSquares(self, num):
        result=[0]*len(num)
        i=0
        j=len(num)-1

        k=len(num)-1

        while(i<=j):
            if(abs(num[i])>abs(num[j])):
                result[k]=num[i]*num[i]
                i=i+1
            else:
                result[k]=num[j]*num[j]
                j=j-1
            k=k-1
        return result
        

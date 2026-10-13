class Solution(object):
    def helper(self, i, j, s):
        while(i<j):
            if s[i]!=s[j]:
                return False
            i=i+1
            j=j-1
        return True

    def validPalindrome(self, s):
        
        i=0
        j=len(s)-1

        while(i<j):
            l=s[i]
            r=s[j]

            if l!=r:
                return self.helper(i+1, j, s) or self.helper(i, j-1, s)
            else:
                i=i+1
                j=j-1
        return True
        

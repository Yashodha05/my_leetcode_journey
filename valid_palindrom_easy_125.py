class Solution(object):
    def isPalindrome(self, s):
        i=0
        j=len(s)-1
        while(i<j):
            l=s[i]
            r=s[j]

            if not l.isalnum():
                i=i+1
                continue
            if not r.isalnum():
                j=j-1
                continue
            if l.lower()!=r.lower():
                return False
            i=i+1
            j=j-1
        return True

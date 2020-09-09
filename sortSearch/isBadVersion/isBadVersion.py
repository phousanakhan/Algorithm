# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1 #not zero because lowest version is one
        right = n
        while (left < right):
            mid = left + (right - left)//2
            if isBadVersion(mid) == False:
                #go to the right
                left = mid + 1
            else:
                right = mid #mid not (mid-1) because of < not =< while condition
                #go to the left
        return(left) #end of search
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        '''
        --Intuition--
        
        (A[0]+K, A[1]+K, ..., A[i]+K, A[i+1]-K, ..., A[n]-K)
        
        for each element i:
            largest ==> A[i]+k or A[n]-K
            smallest ==> A[0]+K or A[i+1]-K
            
        --Intuition Part 1: Left & Right of a "Point"
        
            1. Consider a point 
            2. Any element to the left of it we add k; any element to the right we subtract k
            3. To the left of a point; there exist an array of A[0]+K...A[i]+K
            4. To the right of a point; there exist an array of A[i+1]-K...A[n]-K
            
        --Intuition Part 2: left segment of "Point"
            1. The largest element of the left segment of a point is A[i]+K
            2. The smallest element of the left segment of a point is A[0]+K
            
        --Intuition Part 3: right segment of "Point"
            1. The largest element of the right segment of a point is A[n]-K
            2. The smallest element of the right segment of a point is A[i+1]-K
            
        --Combining Intuition 2&3
            1. The largest element is max(A[i]+K, A[n]-K)
            2. The smallest element is min(A[0]+K, A[i+1]-K)
        
        '''
        nums = sorted(nums)
        left_most = nums[0] + k
        right_most = nums[len(nums)-1] - k
        ret = nums[-1] - nums[0] #largest score as default
        
        for index,value in enumerate(nums[0: len(nums)-1]):
            largest = max(nums[index]+k, right_most)
            smallest = min(left_most, nums[index+1]-k)
            ret = min(ret, largest-smallest)
            print(ret, smallest, largest, largest-smallest)
            
        return ret

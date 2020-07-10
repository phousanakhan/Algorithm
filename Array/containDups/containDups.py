class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict0 = {}
        for i in nums:
            if i in dict0:
                return(True)
            else:
                dict0[i] = 1
        return(False)
        

        
        #OR
        '''
        if len(set(nums)) == len(nums):
            return(False)
        else:
            return(True)
        '''
        
        #OR 
        '''
        return(len(set(nums)) != len(nums))
        '''
        
        #OR
        '''
        if (nums == []):
            return(False)
        nums0 = sorted(nums)
        for index,value in enumerate(nums0):
            try:
                if nums0[index] == nums0[index+1]:
                    return(True)
            except:
                return(False)
        '''
            

            

        


            

            
            
       

                
         
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        dictTask = {}
        for task in tasks:
            if task not in dictTask:
                dictTask[task] = 1
            else:
                dictTask[task] += 1
                
        maxList = sorted(dictTask.values(), reverse = True)
        
        i = 0
        counter = 0 #counter is used to handle multiple maximum case
                                             
        while i < len(maxList) and maxList[i] == maxList[0]:                                
            counter += 1
            i += 1
            
        ret = (maxList[0] - 1) * (n + 1) + counter  ##minimum case
        
        return max(ret, len(tasks))

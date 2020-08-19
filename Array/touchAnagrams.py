class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tempList = []
        finalList = []
        for index,letter in enumerate(strs):
            strs[index] = ''.join(sorted(letter))
            tempList.append((strs[index], letter))
            

        starter = 0
        tempList = sorted(tempList)
        dict0 = {}
        for index,tup in enumerate(tempList):
            if tempList[index][0] not in dict0:
                dict0[tempList[index][0]] = [tempList[index][1]]
            else:
                dict0[tempList[index][0]].append(tempList[index][1])
                
        for i in dict0:
            finalList.append(dict0[i])
            
        return(finalList)

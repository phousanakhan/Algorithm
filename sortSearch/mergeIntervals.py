class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) <= 1:
            return intervals

        intervals = sorted(intervals)
        finalList = []
        currentInterval = intervals[0]
        finalList.append(intervals[0])

        for index,valuePair in enumerate(intervals):
            currentBegin = currentInterval[0]
            currentEnd = currentInterval[1]
            nextBegin = valuePair[0]
            nextEnd = valuePair[1]

            print(currentEnd, nextBegin)
            if currentEnd >= nextBegin:
                currentInterval[1] = max(currentEnd, nextEnd)
            else:
                currentInterval = valuePair
                finalList.append(currentInterval)
                
        return finalList

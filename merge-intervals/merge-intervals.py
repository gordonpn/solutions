class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        index = 0
        intervals.sort()
        
        while index <= len(intervals) - 1:
            if index + 1 < len(intervals) and intervals[index][1] >= intervals[index + 1][0]:
                intervals[index] = [intervals[index][0], max(intervals[index][1], intervals[index + 1][1])]
                intervals.pop(index + 1)
            else:
                index += 1
            
        return intervals
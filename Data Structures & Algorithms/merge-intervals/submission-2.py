class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []

        intervals = sorted(intervals, key=lambda item: item[0])
        results = []
        merged_interval = intervals[0]

        for interval in intervals: 

            if merged_interval[1] >= interval[0]:
                merged_interval[0] = min(merged_interval[0], interval[0])
                merged_interval[1] = max(merged_interval[1], interval[1])
            else:
                results.append(merged_interval)
                merged_interval = interval
        
        results.append(merged_interval)

        # print(merged_interval)

        return results

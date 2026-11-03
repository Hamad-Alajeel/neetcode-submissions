class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        cur_itv = None
        for itv in intervals:
            # breakpoint()
            if cur_itv is None:
                cur_itv = itv
            elif cur_itv[1] >= itv[0] or itv[0] <= cur_itv[1]:
                cur_itv = [min(cur_itv[0],itv[0]),max(cur_itv[1],itv[1])]
            elif cur_itv[1] < itv[0]:
                # breakpoint()
                res.append(cur_itv)
                cur_itv = itv
        # breakpoint()
        res.append(cur_itv)
        return res
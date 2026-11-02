class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = Counter(tasks)
        maxHeap = [-val for val in taskCount.values()]
        heapq.heapify(maxHeap)
        q = deque()

        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    q.append((n+time,cnt))
            if q and q[0][0] == time:
                heapq.heappush(maxHeap,q.popleft()[1])
            
        return time
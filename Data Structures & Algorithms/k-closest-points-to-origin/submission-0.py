class Solution:
    def distance(self, point):
        # here we will calculate the distance of a point to the origin
        return math.sqrt(point[0]**2 + point[1]**2)

    def find_points(slef,points,heap,k):
        return [points[pos[0]] for pos in heap[:k]]
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ## Here we first create an empty list of size k
        heap = [None] * k
        ## then we begin iterating across all points
        for idx,point in enumerate(points):
            dist = self.distance(point)
            ## now we iterate accross all the list (if we bump into a None value we insert it there, otherwise we have a value that is greater than the euclidean distance
            ## of the current point we are on, we need to insert the current point at that index and simply continue onwards)
            for i,val in enumerate(heap):
                if i == k:
                    break
                elif val == None:
                    heap[i] = (idx,dist)
                    break
                elif val[1] >= dist:
                    heap.insert(i,(idx,dist))
                    break
                else:
                    continue
        return self.find_points(points,heap,k)
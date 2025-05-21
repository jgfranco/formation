"""
https://leetcode.com/problems/smallest-number-in-infinite-set/description/?envType=study-plan-v2&envId=leetcode-75
"""

class SmallestInfiniteSet:

    import heapq

    def __init__(self):
        self.current = 1
        self.minHeap = []
        self.addedBack = set()
        

    def popSmallest(self) -> int:
        if len(self.minHeap) > 0:
            smallest = heapq.heappop(self.minHeap)
            self.addedBack.remove(smallest)
            return smallest
        
        val = self.current
        self.current += 1
        return val
        

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.addedBack:
            heapq.heappush(self.minHeap, num)
            self.addedBack.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
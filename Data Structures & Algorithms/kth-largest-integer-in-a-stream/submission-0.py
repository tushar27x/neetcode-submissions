class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums     
        self.kLargest = heapq.nlargest(k, nums)   

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.kLargest = heapq.nlargest(self.k, self.nums)

        return self.kLargest[self.k-1]

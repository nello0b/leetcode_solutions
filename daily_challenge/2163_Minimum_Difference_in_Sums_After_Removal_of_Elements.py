# https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/description/?envType=daily-question&envId=2025-07-18

"""
You are given a 0-indexed integer array nums consisting of 3 * n elements.

You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:

The first n elements belonging to the first part and their sum is sumfirst.
* The next n elements belonging to the second part and their sum is sumsecond.
* The difference in sums of the two parts is denoted as sumfirst - sumsecond.

For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.
Return the minimum difference possible between the sums of the two parts after the removal of n elements.

Constraints:

* nums.length == 3 * n
* 1 <= n <= 105
* 1 <= nums[i] <= 105
"""

from typing import List
import heapq

import heapq

import heapq

class MinHeap:
    def __init__(self, initial=None):
        if initial is None:
            self._heap = []
        else:
            self._heap = initial[:]
            heapq.heapify(self._heap)

    def push(self, val):
        heapq.heappush(self._heap, val)

    def pop(self):
        return heapq.heappop(self._heap)

    def peek(self):
        return self._heap[0] if self._heap else None

    def __len__(self):
        return len(self._heap)

    def is_empty(self):
        return len(self._heap) == 0
    
    def k_min(self, k):
        return heapq.nsmallest(k, self._heap)


class MaxHeap(MinHeap):
    def __init__(self, initial=None):
        # Negate all values for max-heap behavior, then pass to super
        if initial is not None:
            initial = [-x for x in initial]
        super().__init__(initial)

    def push(self, val):
        super().push(-val)

    def pop(self):
        return -super().pop()

    def peek(self):
        val = super().peek()
        return -val if val is not None else None

    def k_max(self, k):
        negated_k_min = super().k_min(k)
        return [-x for x in negated_k_min]
    
    def k_min(self, k):
        raise 

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = int(len(nums) / 3)
        start = MaxHeap(nums[:n])
        end = MinHeap(nums[2*n:])
        
        
        
        min_dif = sum(nums[:n]) - sum(nums[2*n:])
        for i, _ in enumerate(nums[:2*n], n):
            dif = sum(k_min_sort(nums[:i],n)) - sum(k_max_sort(nums[i:],n))
            if dif < min_dif:
                min_dif = dif
                
        return min_dif
    
    
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    nums1 = [3, 1, 2]
    nums2 = [7, 9, 5, 8, 1, 3]
    
    # Running the test cases
    print("Test case 1:")
    result1 = solution.minimumDifference(nums1)
    print(f"Result for nums1 = {nums1}: {result1}")
    
    print("\nTest case 2:")
    result2 = solution.minimumDifference(nums2)
    print(f"Result for nums2 = {nums2}: {result2}")
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
* 1 <= n <= 10^5
* 1 <= nums[i] <= 10^5
"""

# Run:
# python3 2163_Minimum_Difference_in_Sums_After_Removal_of_Elements.py 

from typing import List
from heapq import heappush, heappop

# maintaint the maximum sum because when I add it will remove the smallest
class MinHeap:
    def __init__(self, initial: List[int], n: int):
        self.heap = []
        self.curr_sum  = 0
        self.n = n
        for x in initial:
            self.insert(x)

    def insert(self, val: int) -> 'MinHeap':
        heappush(self.heap, val)
        self.curr_sum += val

        if len(self.heap) > self.n:
            popped = heappop(self.heap)
            self.curr_sum -= popped
        return self

# maintaint the mimimum sum because when I add it will remove the largest
class MaxHeap:
    def __init__(self, initial: List[int], n: int):
        self.heap = []
        self.curr_sum  = 0
        self.n = n
        for x in initial:
            self.insert(x)

    def insert(self, val: int) -> 'MaxHeap':
        heappush(self.heap, -val)
        self.curr_sum += val

        if len(self.heap) > self.n:
            popped = -heappop(self.heap)
            self.curr_sum -= popped
        return self


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        start = MaxHeap(nums[:n], n)
        end = MinHeap(nums[2*n:], n)

        
        start_min_sums = [start.curr_sum]
        end_max_sum = [end.curr_sum]
        for num in nums[n:2*n]:
            start.insert(num)
            start_min_sums.append(start.curr_sum)
            
        for num in nums[n:2*n][::-1]:
            end.insert(num)
            end_max_sum.append(end.curr_sum)
        
        end_max_sum.reverse()
        
        min_dif = start_min_sums[0] - end_max_sum[0]
        for i in range(len(start_min_sums)):
            dif = start_min_sums[i] - end_max_sum[i]
            if dif < min_dif:
                min_dif = dif

        return min_dif
    
    
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    tests = [
        (-1,[3, 1, 2]),
        (1,[7, 9, 5, 8, 1, 3]),
        (-337,[47,26,21,40,3,20,12,19,1,11,37,49,50,29,23,32,27,10,49,24,44,43,46,27,2,3,41,35,10,49,38,44,6,27,27,43,5,36,37,16,5,30,12,15,6,50,44,40,17,45,24,33,32,4,35,37,15,17,13,21]),
        ]
    
    # Running the test cases
    for i, (expected, nums) in enumerate(tests, 1):
        print(f"Test case {i}:")
        result = solution.minimumDifference(nums)
        if len(nums) < 20:
            nums_str = f"{nums}"
        else: 
            nums_str = f"[{', '.join(f'{num}' for num in nums[:20])}...]"
        status = "✅" if result == expected else "❌"
        sign = "=" if result == expected else "≠"
        print(f"Result for nums1 = {nums_str}: {result} {sign} {expected} {status}")

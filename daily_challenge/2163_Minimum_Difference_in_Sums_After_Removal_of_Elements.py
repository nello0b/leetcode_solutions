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
from heapq import heappush, heappop, heapify


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        # Max heap (left part): store negatives to simulate max-heap
        max_heap = [-num for num in nums[:n]]
        heapify(max_heap)
        max_sum = -sum(max_heap)

        # Preallocate left sums
        left_sums = [0] * (n + 1)
        left_sums[0] = max_sum

        for i in range(n):
            num = nums[n + i]
            heappush(max_heap, -num)
            max_sum += num
            popped = -heappop(max_heap)
            max_sum -= popped
            left_sums[i + 1] = max_sum

        # Min heap (right part)
        min_heap = nums[2 * n:]
        heapify(min_heap)
        min_sum = sum(min_heap)

        # Preallocate right sums
        right_sums = [0] * (n + 1)
        right_sums[n] = min_sum

        for i in range(n):
            num = nums[2 * n - 1 - i]
            heappush(min_heap, num)
            min_sum += num
            popped = heappop(min_heap)
            min_sum -= popped
            right_sums[n - 1 - i] = min_sum

        # Find the minimum difference
        min_diff = left_sums[0] - right_sums[0]
        for i in range(n + 1):
            diff = left_sums[i] - right_sums[i]
            if diff < min_diff:
                min_diff = diff

        return min_diff
    
    
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

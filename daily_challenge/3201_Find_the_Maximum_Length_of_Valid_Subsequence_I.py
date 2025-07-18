# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/description/?envType=daily-question&envId=2025-07-16

from typing import List, Tuple

# (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2

# [1,2,2,3,3,4] -> 4
# (1 + 2) % 2 = 1

# 2 is a constant, so it means that there are only 2 cases:
# (sub[0] + sub[1]) % 2 == 1
# or:
# (sub[0] + sub[1]) % 2 == 0
# we can focus ourself on optemizing for those 2 cases, and dont need to do a fancy code that will with for N equal anything, just N = 2.

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        alt = 1
        even = 1 if nums[0] % 2 == 0 else 0
        
        prev = nums[0]
        for num in nums[1:]:
            if num % 2 == 0:
                even += 1
            if num % 2 != prev % 2:
                alt += 1
                prev = num
            
        odd = len(nums) - even
        
        return max(even, odd, alt)


# Main function to test the solution
def main():
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([1, 2, 2, 3, 3, 4], 4),  # Example from the problem description
        ([1, 3, 5, 7], 4),        # All odd numbers
        ([2, 4, 6, 8], 4),        # All even numbers
        ([1, 2, 3, 4, 5], 5),     # Alternating odd and even
        ([1, 1, 1, 1], 4),        # All identical odd numbers
        ([2, 2, 2, 2], 4),        # All identical even numbers
        ([1, 2], 2),              # Minimum length input
        ([2, 1, 2, 1, 2], 5),     # Alternating pattern
        ([2, 39, 23], 2),
        ([4,51,68],3)
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        result = solution.maximumLength(nums)
        print(f"Test case {i + 1}: nums = {nums}")
        print(f"Expected: {expected}, Got: {result}")
        assert result == expected, f"Test case {i + 1} failed! got result = {result}, while expected = {expected}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    main()
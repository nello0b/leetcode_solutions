// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/description/?envType=daily-question&envId=2025-07-17

/*
You are given an integer array nums and a positive integer k.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
Return the length of the longest valid subsequence of num
*/

// Run:
// gcc 3202_Find_the_Maximum_Length_of_Valid_Subsequence_II.c -o solution && ./solution

#include <stdio.h>
#include <assert.h>
#include <string.h>

int maximumLength(int *nums, int numsSize, int k)
{
    // setting up the dp
    int dp[numsSize * k];
    memset(dp, 0, sizeof(dp));

    int maxLength = 1;
    int mode;
    int i_mode;
    int j_mode_plus_one;
    int len;
    int *dpI = (int *)dp + k;
    int *dpJ;
    int *dpI_plus_mode;
    int *dpJ_plus_mode;
    for (int i = 1; i < numsSize; i++, dpI += k)
    {
        dpJ = (int *)dpI - k;
        for (int j = i - 1; j >= 0; j--, dpJ -= k)
        {
            mode = (nums[j] + nums[i]) % k;
            dpI_plus_mode = dpI + mode;
            dpJ_plus_mode = dpJ + mode;
            i_mode = *dpI_plus_mode ? *dpI_plus_mode : 1;
            j_mode_plus_one = *dpJ_plus_mode ? *dpJ_plus_mode + 1 : 2;
            len = i_mode > j_mode_plus_one ? i_mode : j_mode_plus_one;
            *dpI_plus_mode = len;
            maxLength = len > maxLength ? len : maxLength;
        }
    }

    return maxLength;
}

int main()
{
    // arrays
    int nums1[] = {1, 2, 3, 4, 5};
    int nums2[] = {1, 4, 2, 3, 1, 4};
    int nums3[] = {1, 2, 3, 10, 2};
    int nums4[] = {1, 5, 9, 2, 8};
    int nums5[] = {4, 10, 6, 5, 10};
    int nums6[] = {1, 2, 5, 7, 9, 8, 8};
    int nums7[] = {1, 7, 9, 10, 8, 7, 10};

    // parameters

    int *numss[] = {nums1, nums2, nums3, nums4, nums5, nums6, nums7};
    int sizes[] = {5, 6, 5, 5, 5, 7, 7};
    int ks[] = {2, 3, 6, 2, 2, 7, 6};
    int expected[] = {5, 4, 3, 3, 4, 3, 4};
    int tests = sizeof(numss) / sizeof(numss[0]);

    for (int i = 0; i < tests; i++)
    {
        printf("Running case %d:\n", i + 1);
        int result = maximumLength(numss[i], sizes[i], ks[i]);
        printf("Test case %d: Result = %d, Expected = %d\n", i + 1, result, expected[i]);
        assert(result == expected[i]);
    }

    printf("All test cases passed!\n");
    return 0;
}

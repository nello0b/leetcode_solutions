package top_150;
// https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

// Compile and run:
// javac 88_Merge_Sorted_Array.java && java Solution

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1;     // the index for nums1
        int j = n - 1;     // the index for nums2
        int k = m + n - 1; // the index for merged position in nums1
        
        // Merge from the end, comparing elements
        while (i >= 0 && j >= 0){
            if (nums1[i] > nums2[j]) {
                nums1[k] = nums1[i];
                i--;
            } 
            else{
                nums1[k] = nums2[j];
                j--;
            }
            k--;
        }
        
        // Copy remaining elements from nums2 (if any)
        while (j >= 0) {
            nums1[k] = nums2[j];
            j--;
            k--;
        }
    }
    
    public static void print_array(int[] arr) {
        System.out.print("[");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if( i < arr.length - 1) {
                System.out.print(" , ");
            }
        }
        System.out.println("]");
    }
    
    public static void main(String[] args) {
        Solution solution = new Solution();
    
        // Test case 1: Basic merge
        int[] nums1_1 = {1, 2, 3, 0, 0, 0};
        int[] nums2_1 = {2, 5, 6};
        solution.merge(nums1_1, 3, nums2_1, 3);
        System.out.println("Test 1: " + java.util.Arrays.toString(nums1_1));
        
        // Test case 2: nums1 is empty
        int[] nums1_2 = {0};
        int[] nums2_2 = {1};
        solution.merge(nums1_2, 0, nums2_2, 1);
        System.out.println("Test 2: " + java.util.Arrays.toString(nums1_2));
        
        // Test case 3: nums2 is empty
        int[] nums1_3 = {1};
        int[] nums2_3 = {};
        solution.merge(nums1_3, 1, nums2_3, 0);
        System.out.println("Test 3: " + java.util.Arrays.toString(nums1_3));
        
        // Test case 4: nums1 = [2,0], m = 1, nums2 = [1], n = 1
        int[] nums1_4 = {2, 0};
        int[] nums2_4 = {1};
        solution.merge(nums1_4, 1, nums2_4, 1);
        System.out.println("Test 4: " + java.util.Arrays.toString(nums1_4));
        
        // Test case 5: All elements from nums2 are smaller
        int[] nums1_5 = {4, 5, 6, 0, 0, 0};
        int[] nums2_5 = {1, 2, 3};
        solution.merge(nums1_5, 3, nums2_5, 3);
        System.out.println("Test 5: " + java.util.Arrays.toString(nums1_5));
        
        // Test case 6: All elements from nums1 are smaller
        int[] nums1_6 = {1, 2, 3, 0, 0, 0};
        int[] nums2_6 = {4, 5, 6};
        solution.merge(nums1_6, 3, nums2_6, 3);
        System.out.println("Test 6: " + java.util.Arrays.toString(nums1_6));
        
        // Test case 7: Duplicate elements
        int[] nums1_7 = {1, 2, 2, 0, 0, 0};
        int[] nums2_7 = {2, 2, 3};
        solution.merge(nums1_7, 3, nums2_7, 3);
        System.out.println("Test 7: " + java.util.Arrays.toString(nums1_7));
        
        // Test case 8: Single element arrays
        int[] nums1_8 = {2, 0};
        int[] nums2_8 = {1};
        solution.merge(nums1_8, 1, nums2_8, 1);
        System.out.println("Test 8: " + java.util.Arrays.toString(nums1_8));
        
        // Test case 9: Negative numbers
        int[] nums1_9 = {-1, 0, 1, 0, 0, 0};
        int[] nums2_9 = {-2, 2, 3};
        solution.merge(nums1_9, 3, nums2_9, 3);
        System.out.println("Test 9: " + java.util.Arrays.toString(nums1_9));
        
        // Test case 10: Larger arrays
        int[] nums1_10 = {1, 3, 5, 7, 9, 0, 0, 0, 0};
        int[] nums2_10 = {2, 4, 6, 8};
        solution.merge(nums1_10, 5, nums2_10, 4);
        System.out.println("Test 10: " + java.util.Arrays.toString(nums1_10));
    }
}
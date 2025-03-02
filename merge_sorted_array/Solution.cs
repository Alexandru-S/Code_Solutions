public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        //  nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        // has to be copied in place
        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;
        while(i >= 0 && j >= 0){
            if(nums1[i] > nums2[j]){
                nums1[k--] = nums1[i--];
            }else{
                nums1[k--] = nums2[j--];
            }
        }
        while(j >= 0){ // copy rest of array 
            nums1[k--] = nums2[j--];
        }
    }
}
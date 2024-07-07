class Solution {
    public int[] rearrangeArray(int[] nums) {
        int result[] = new int[nums.length];
        int positive_index = 0;
        int negative_index = 1;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] > 0){
                result[positive_index] = nums[i];
                positive_index = positive_index + 2;
            }
            else{
                result[negative_index] = nums[i];
                negative_index = negative_index + 2;
            }
        }
        return result;
    }
}
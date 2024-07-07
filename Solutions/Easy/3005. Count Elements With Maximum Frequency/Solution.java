class Solution {
    public int maxFrequencyElements(int[] nums) {
        int max = 0;
        for (int n : nums) if (n > max) max = n;

        int[] counts = new int[max + 1];
        for (int n : nums) counts[n]++;

        int freq = 0, res = 0;
        for (int count : counts) {
            if (count == freq) {
                res += freq;
            } else if (count > freq) {
                res = freq = count;
            }
        }
        return res;
    }
}
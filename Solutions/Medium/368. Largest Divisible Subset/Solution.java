import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        Arrays.sort(nums);
        
        int n = nums.length;
        int[] dp = new int[n];
        int[] pre = new int[n];
        int maxLength = 0;
        int maxEnding = -1;
        for ( int i = 0; i < n; i++ ) {
            int max = 1;
            int preEnding = -1;
            for ( int j = 0; j < i; j++ ) {
                if ( nums[i]%nums[j] != 0 ) continue;
                
                if ( dp[j]+1 > max ) {
                    max = dp[j]+1;
                    preEnding = j;
                }
            }
            
            dp[i] = max;
            pre[i] = preEnding;
            
            if ( dp[i] > maxLength ) {
                maxLength = dp[i];
                maxEnding = i;
            }
        }
        
        List<Integer> ans = new ArrayList<>();
        while ( maxEnding != -1 ) {
            ans.add(0, nums[maxEnding]);
            maxEnding = pre[maxEnding];
        }
        
        return ans;
    }
}

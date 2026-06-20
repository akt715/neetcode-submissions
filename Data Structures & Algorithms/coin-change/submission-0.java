class Solution {
    private int[][] memo;
    
    public int coinChange(int[] coins, int amount) {
        // Initialize memo
        // memo[i][j] = min coins to form amount j using coins[i...n-1]
        memo = new int[coins.length][amount + 1];
        for (int i = 0; i < coins.length; i++) {
            for (int j = 0; j <= amount; j++) {
                memo[i][j] = -1; // -1 indicates not computed yet
            }
        }

        int result = dfs(coins, 0, amount);
        return result == Integer.MAX_VALUE ? -1 : result;
    }
    
    private int dfs(int[] coins, int index, int amount) {
        // Base Cases
        if (amount == 0) return 0; // 0 coins needed to form 0 amount
        if (index == coins.length) return Integer.MAX_VALUE; // no more coins to use

        if (memo[index][amount] != -1) return memo[index][amount];

        int res = Integer.MAX_VALUE;

        // Include current coin if possible
        if (coins[index] <= amount) {
            int includeRes = dfs(coins, index, amount - coins[index]);
            if (includeRes != Integer.MAX_VALUE) {
                res = Math.min(res, 1 + includeRes);
            }
        }

        // Exclude current coin
        int excludeRes = dfs(coins, index + 1, amount);
        res = Math.min(res, excludeRes);

        memo[index][amount] = res;
        return res;
    }
}
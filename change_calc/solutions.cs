   // DP
    public static long getWays(int n, List<long> c)
{
    c.Sort();
    var memo = new Dictionary<(int start, int remaining), long>();
    long Dfs(int start, int remaining) {
        if (remaining == 0) {
            return 1;
        }
        var key = (start, remaining);
        if (memo.TryGetValue(key, out var cached)) {
            return cached;
        }
        long total = 0;
        for (int i = start; i < c.Count; i++) {
            long coin = c[i];
            if (coin > remaining) {
                break;
            }
            total += Dfs(i, remaining - (int)coin);
        }
        memo[key] = total;
        return total;

    }
    return Dfs(0, n);

}
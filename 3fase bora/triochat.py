n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

inf = 10**18
dp = [[inf] * (k + 1) for _ in range(n + 1)]

dp[1][0] = 0
for j in range(1, k + 1):
    dp[1][j] = inf

for i in range(2, n + 1):
    for j in range(k + 1):
        if 3 * j > i:
            dp[i][j] = inf
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i - 2][j - 1] + (a[i - 1] - a[i - 2]) ** 2)

print(dp[n][k])

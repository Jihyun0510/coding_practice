def solution(m, n, puddles):
    puddles = [[q,p] for [p, q] in puddles]

    dp = [[0] * (m+1) for _ in range(n+1)]
  
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1:
                dp[i][j] = 1
                continue
            # 0 => False
            if [i,j] in puddles:
                dp[i][j] = False
                continue
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    
    print(dp)
    return dp[n][m]
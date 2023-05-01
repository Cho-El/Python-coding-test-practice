def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        defaultDP = dp[i - 1] + (dp[i - 2] * 2) + (dp[i - 3] * 5)
        
        if i >= 4:
            sub = 4
            while sub <= i:
                defaultDP += 2 * dp[i - sub]
                sub += 3
        if i >= 5:
            sub = 5
            while sub <= i:
                defaultDP += 2 * dp[i - sub]
                sub += 3
        if i >= 6:
            sub = 6
            while sub <= i:
                defaultDP += 4 * dp[i - sub]
                sub += 3
            
        dp[i] = max(dp[i], defaultDP)
        
    return dp[n] % 1000000007

def solution2(n):
    
    
    if n==1: return 1
    elif n==2: return 3
    elif n==3: return 10
    
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    dp[2]=3
    dp[3]=10
    dp[4]=23
    
    for i in range(5,n+1):
        dp[i] = (dp[i-1]+2*dp[i-2]+6*dp[i-3]+dp[i-4]-dp[i-6]) % 1000000007
    return dp[-1]
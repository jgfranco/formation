
#recursive approach
def fib(k):
    if k <= 1: return k
    return fib(k-1) + fib(k-2)

print("recursive testing")
print(fib(1) == 1)
print(fib(2) == 1)
print(fib(3) == 2)
print(fib(4) == 3)
print(fib(5) == 5)
print(fib(6) == 8)
print(fib(7) == 13)
print(fib(8) == 21)
#print(fib(1000))

def fibIterative(k):
    if k <= 1: return k
    a , b = 0, 1

    for _ in range(2, k + 1):
        a, b = b, a+b

    return b

print("iterative testing")
print(fibIterative(1) == 1)
print(fibIterative(2) == 1)
print(fibIterative(3) == 2)
print(fibIterative(4) == 3)
print(fibIterative(5) == 5)
print(fibIterative(6) == 8)
print(fibIterative(7) == 13)
print(fibIterative(8) == 21)
#print(fibIterative(1000))

def fibMemo(k):
    
    memo = {}
    def helper(k):
        if k in memo:
            return memo[k]
        
        if k <= 1:
            memo[k] = k
        else:
            memo[k] = helper(k-1) + helper(k-2)
        
        return memo[k]
    
    return helper(k)

print("memoization testing")
print(fibMemo(1) == 1)
print(fibMemo(2) == 1)
print(fibMemo(3) == 2)
print(fibMemo(4) == 3)
print(fibMemo(5) == 5)
print(fibMemo(6) == 8)
print(fibMemo(7) == 13)
print(fibMemo(8) == 21)
#print(fibMemo(1000))

def fibDP(k):
    dp = [0] * (k+1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, k+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[k]


print("DP testing")
print(fibDP(1) == 1)
print(fibDP(2) == 1)
print(fibDP(3) == 2)
print(fibDP(4) == 3)
print(fibDP(5) == 5)
print(fibDP(6) == 8)
print(fibDP(7) == 13)
print(fibDP(8) == 21)

def fibDPOptimized(k):
    if k <= 1: return k
    a = 0
    b = 1

    for _ in range(2, k+1):
        a, b = b, a+b
    
    return b


print("DP optimized testing")
print(fibDPOptimized(1) == 1)
print(fibDPOptimized(2) == 1)
print(fibDPOptimized(3) == 2)
print(fibDPOptimized(4) == 3)
print(fibDPOptimized(5) == 5)
print(fibDPOptimized(6) == 8)
print(fibDPOptimized(7) == 13)
print(fibDPOptimized(8) == 21)

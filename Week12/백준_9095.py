import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())


def solve(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    # n이 4부터는 n-1, n-2, n-3을 더한 값이 해당 값이 됨
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]


for _ in range(T):
    n = int(input())
    result = solve(n)
    print(result)


# 왜 아래는 index 에러가 계속?

# T = int(input())

# for _ in range(T):
#     n = int(input())
#     dp = [0]*(n+1)
#     dp[1] = 1
#     dp[2] = 2
#     dp[3] = 4

#     if n > 3:  # n이 4부터는 n-1, n-2, n-3을 더한 값이 해당 값이 됨
#         for i in range(4, n+1):
#             dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

#     print(dp[n])

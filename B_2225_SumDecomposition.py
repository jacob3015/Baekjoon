"""B 2225 합분해(Sum Decomposition)
Problem:
    0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성하시오.
    덧셈의 순서가 바뀐 경우는 다른 경우로 센다. 또한 한 개의 수를 여러 번 쓸 수도 있다.

Input:
    첫째 줄에 두 정수 N, K가 주어진다.
    N, K는 200 이하의 자연수이다.

Output:
    첫째 줄에 답을 10억으로 나눈 나머지를 출력한다.
"""

def solution():
    """0부터 N까지 정수 K개를 더해 합이 N이 되는 경우의 수를 구해 출력한다.
    Extra explanation:
        N과 K의 관계를 찾아보는 것으로 점화식을 도출해낼 수 있다.
        N이 1일 때, K와 관계없이 경우의 수는 K이다.
        K가 1일 때, N과 관계없이 경우의 수는 1이다.
        0부터 N까지 정수 K개를 더해 합이 N이 되는 경우의 수를 구해 표로 나타낸 뒤 이를 점화식으로 풀이하면,
        result[K][N] = result[K-1][N] + result[K][N-1]을 만족한다.
    
    Variables:
        INT_MAX : 10억
        N, K : inputs
        result : 0부터 N까지 정수 K개를 더해 합이 N이 되는 경우의 수
    
    Example:
        >>> 20 2
        >>> 21
    """
    INT_MAX = 10**9
    N, K = map(int, input().split())
    result = [[0 for _ in range(N+1)] for _ in range(K+1)]

    for i in range(1, K+1):
        result[i][1] = i

    for i in range(1, N+1):
        result[1][i] = 1

    for i in range(2, K+1):
        for j in range(2, N+1):
            result[i][j] = result[i-1][j] + result[i][j-1]
            
    print(result[K][N]%INT_MAX)
    
solution()
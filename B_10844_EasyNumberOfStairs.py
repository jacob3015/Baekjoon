"""B 10844 쉬운 계단 수(Easy Number of Stairs)
Problem:
    45656이란 수를 보자.
    이 수는 인접한 모든 자리수의 차이가 1이 난다.
    이런 수를 계단 수라고 한다.
    세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.
    N이 주어졌을 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는지 프로그램을 작성하시오.
    0으로 시작하는 수는 없다.

Input:
    첫째 줄에 N이 주어진다.
    N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

Output:
    첫째 줄에 정답을 10^9(10억) 으로 나눈 나머지를 출력한다.
"""

def solution():
    """길이가 N인 계단 수의 개수를 구해 출력한다.
    Extra explanation:
        Dynamic programming의 memoization을 활용해 문제를 해결한다.
        주어진 수의 길이를 i, i-1번째 수를 j라고 할 때,
        j가 0일 때의 계단 수의 개수는 길이가 i-1이고 i-2번째 수가 1인 계단 수의 개수와 같다.
        j가 9일 때의 계단 수의 개수는 길이가 i-1이고 i-2번째 수가 8인 계단 수의 개수와 같다.
        j가 1~8일 때 계단 수의 개수는 길이가 i-1이고 i-2번째 수가 j+1 또는 j-1 일 때 계단 수의 개수와 같다.
    
    Variables:
        INT_MAX : 결과값의 크기를 줄이기 위한 정수, 10억
        N : 주어진 수의 길이
        result : 계단 수의 개수, result[자리수(i)][i-1번째 수]
    
    Example:
        >>> 3   : input N
        >>> 32  : output result
    """
    INT_MAX = 10**9
    N = int(input())

    result = [[0]*10 for _ in range(N+1)]
    for i in range(1, 10):
        result[1][i] = 1

    for i in range(2, N+1):
        for j in range(10):
            if j < 1:
                result[i][j] = result[i-1][1]
            elif 0 < j < 9:
                result[i][j] = result[i-1][j-1] + result[i-1][j+1]
            else:
                result[i][j] = result[i-1][8]

    print(sum(result[N])%INT_MAX)

solution()
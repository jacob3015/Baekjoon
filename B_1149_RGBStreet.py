"""B 1149 RGB 거리(RGB Street)
Problem:
    RGB거리에는 집이 N개 있다.
    거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.
    집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다.
    각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.
    1. 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
    2. N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
    3. i번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다. (2 <= i <= N-1)
Input:
    첫째 줄에 집의 수 N이 주어진다.
    둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다.
    집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

Output:
    첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.
"""

def solution():
    """모든 집을 칠하는 비용의 최솟값을 구해 출력한다.

    Variable:
        N : 집의 개수
        prices : N번째 집에 빨강색, 초록색, 파랑색을 칠하는 비용 list
    
    Example:
        >>> 3           : input N
        >>> 26 40 83    : input prices
        >>> 49 60 57
        >>> 13 89 99
        >>> 96          : output result
    """
    N = int(input())
    prices = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, N):
        prices[i][0] += min(prices[i-1][1], prices[i-1][2])
        prices[i][1] += min(prices[i-1][0], prices[i-1][2])
        prices[i][2] += min(prices[i-1][0], prices[i-1][1])
        
    print(min(prices[N-1]))

solution()
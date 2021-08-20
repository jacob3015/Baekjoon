"""B 1699 제곱수의 합(Sum of Squares)
Problem:
    어떤 자연수 N은 그보다 작거나 같은 제곱수들의 합으로 나타낼 수 있다.
    주어진 자연수 N을 제곱수들의 합으로 표현할 때에 그 항의 최소개수를 구하는 프로그램을 작성하시오.

Input:
    첫째 줄에 자연수 N이 주어진다.
    N은 100,000 이하이다.

Output:
    주어진 자연수를 제곱수의 합으로 나타낼 때에 그 제곱수 항의 최소 개수를 출력한다.
"""
import math

def solution():
    """자연수를 재곱수의 합으로 나타낼 때 제곱수 항의 최소 개수를 구해 출력한다.
    Extra explanation:
        DP의 memoization을 활용해 문제를 해결한다.
        최소 개수를 구하기 위해 min() method를 활용해도 답은 구할 수 있지만 시간초과를 피하기 위해 PyPy3로 제출해야한다.
        if문을 활용해 최소 개수를 구하면 Python3로 제출해도 시간초과를 피할 수 있다.
    
    Variables:
        N : 주어진 자연수
        result : 자연수를 제곱수의 합으로 나타낼 때 제곱수 항의 최소 개수 list, memoization을 위한 list
    
    Example:
        >>> 7   : input N
        >>> 4   : output result
    """
    N = int(input())
    result = [i for i in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, int(math.sqrt(i)) + 1):
            if result[i] > result[i-j**2] + 1:
                result[i] = result[i-j**2] + 1
                
    print(result[N])

solution()
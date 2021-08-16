"""B 11053 가장 긴 증가하는 부분 수열(Longest Increasing Subsequence)
Problem:
    수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

Input:
    첫째 줄에 수열 A의 크기 N이 주어진다.
    둘째 줄에는 수열 A를 이루고 있는 A(i)가 주어진다.
    N과 A(i)는 1,000 이하의 자연수이다.

Output:
    첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
"""

def solution():
    """주어진 수열의 가장 긴 증가하는 부분 수열의 길이를 구해 출력한다.
    Extra explanation:
        길이가 i-1인 증가하는 수열의 i-1번째 수보다 큰 수를 i번째 수로 추가하면 길이가 i인 증가하는 수열을 만들 수 있다.
        위 풀이와 DP의 memoization을 활용해 문제를 해결한다.
    
    Variables:
        N : 주어진 수열의 길이
        sequence : 주어진 수열
        result : 주어진 수열의 증가하는 부분 수열의 길이 list, memoization을 위한 list
    
    Example:
        >>> 6                   : input N
        >>> 10 20 10 30 20 50   : input sequence
        >>> 4                   : output result
    """
    N = int(input())
    sequence = list(map(int, input().split()))
    result = [1 for _ in range(N)]

    for i in range(N):
        for j in range(i):
            if sequence[i] > sequence[j]:
                result[i] = max(result[i], result[j]+1)
                
    print(max(result))

solution()
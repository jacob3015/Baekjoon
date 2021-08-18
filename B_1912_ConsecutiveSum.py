"""B 1912 연속합(Consecutive Sum)
Problem:
    n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다.
    단, 수는 한 개 이상 선택해야 한다.

Input:
    첫째 줄에 정수 n이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다.
    수는 -1,000 보다 크거나 같고, 1,000 보다 작거나 같은 정수이다.
    n은 100,000 이하의 자연수이다.

Output:
    첫째 줄에 답을 출력한다.
"""

def solution():
    """주어진 수열의 연속된 부분 수열의 합 중 최댓값을 구해 출력한다.

    Variables:
        n : 주어진 수열의 수 개수
        sequence : 주어진 수열
    
    Example:
        >>> 10                          : input n
        >>> 10 -4 3 1 5 6 -35 12 21 -1  : input sequence
        >>> 33                          : output result
    """
    n = int(input())
    sequence = list(map(int, input().split()))

    for i in range(1, n):
        sequence[i] = max(sequence[i], sequence[i-1] + sequence[i])
        
    print(max(sequence))

solution()
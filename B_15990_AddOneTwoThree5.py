"""B 15990 1, 2, 3 더하기 5(Add One Two Three 5)
Problem:
    정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
    합을 나타낼 때는 수를 1개 이상 사용해야 하며, 같은 수를 두 번 이상 연속 사용하면 안 된다.

Input:
    첫째 줄에 테스트 케이스의 개수 T가 주어진다.
    각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.
    n은 양수이며 100,000 보다 작거나 같다.

Output:
    각 테스트 케이스마다 n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지를 출력한다.
"""
from collections import deque

def solution():
    """n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지를 출력한다.
    Extra explanation:
        Dynamic programming의 memoization 기법을 활용해 문제를 해결한다.
        n을 1, 2, 3의 합으로 나타낼 때 같은 수를 두 번 이상 연속 사용하면 안되므로 마지막에 오는 수의 개수를 memo할 필요가 있다.
        예를 들어, 3을 1, 2, 3의 합으로 나타내면 2+1, 1+2, 3으로 나타낼 수 있으며 마지막에 오는 수는 각각 1, 2, 3이 된다.
        이 때, 마지막에 오는 수의 개수는 1, 2, 3이 각각 1개이다.
        이를 [1의 개수, 2의 개수, 3의 개수] 이런식으로 메모하면 [1, 1, 1]이 된다.
        n을 1, 2, 3의 합으로 나타내는 방법의 수가 A(n)이고, n을 1, 2, 3의 합으로 나타낼 때 마지막에 오는 수의 개수가 C(n)일 때(C(n) = [1의 개수, 2의 개수, 3의 개수]),
        A(n) = (C(n-1)의 2의 개수 + 3의 개수) + (C(n-2)의 1의 개수 + 3의 개수) + (C(n-3)의 1의 개수 + 2의 개수)을 만족한다.
    
    Variables:
        INT_MAX : 결과 값이 커지는 것을 방지하기 위해 나눠주는 수
        T : 테스트 케이스의 개수
        test_case : 테스트 케이스 list
        result : n을 1, 2, 3의 합으로 나타내는 방법의 수 list
        count : n-1, n-2, n-3을 1, 2, 3의 합으로 나타낼 때 마지막에 오는 수의 개수, memoization을 위한 deque
    
    Example:
        >>> 3       : input T
        >>> 4       : input test cases
        >>> 7
        >>> 10
        >>> 3       : output results
        >>> 9
        >>> 27
    """
    INT_MAX = 1000000009
    T = int(input())
    test_case = [int(input()) for _ in range(T)]

    result = [0 for _ in range(max(test_case)+1)]
    result[1], result[2], result[3] = 1, 1, 3

    if max(test_case) < 4:
        for case in test_case:
            print(result[case])
        return

    count = [[0]*3 for _ in range(3)]
    count[0][0], count[1][1] = 1, 1
    for i in range(3):
        count[2][i] = 1
    count = deque(count)
    
    for i in range(4, max(test_case)+1):
        new = [0] * 3
        new[0] = (sum(count[2]) - count[2][0])%INT_MAX
        new[1] = (sum(count[1]) - count[1][1])%INT_MAX
        new[2] = (sum(count[0]) - count[0][2])%INT_MAX

        result[i] = sum(new)%INT_MAX

        count.popleft()
        count.append(new)
    
    for case in test_case:
        print(result[case])
        
solution()
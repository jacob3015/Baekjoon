"""B 15988 1, 2, 3 더하기 3(Add One Two Three 3)
Problem:
    정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

Input:
    첫째 줄에 테스트 케이스의 개수 T가 주어진다.
    각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.
    n은 양수이며 1,000,000 보다 작거나 같다.

Output:
    각 테스트 게이스마다 n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지를 출력한다.
"""

def solution():
    """주어진 테스트 케이스를 1, 2, 3의 합으로 나타내는 방법의 수를 구해 출력한다.
    Extra explanation:
        1, 2, 3의 합으로 나타내는 방법의 수를 A(i)이라 한다면,
        A(i) = A(i-1) + A(i-2) + A(i-3) (i는 정수, 3 < i <= n, A(1) = 1, A(2) = 2, A(3) = 4)를 만족한다.
    
    Variables:
        INT_MAX : n을 1, 2, 3의 합으로 나타내는 방법의 수를 나누는 상수, 1,000,000,009
        T : 테스트 케이스의 개수
        test_case : 테스트 케이스 list
        result : n을 1, 2, 3의 합으로 나타내는 방법의 수 list, memoization을 위한 list
    
    Example:
        >>> 3       : input T
        >>> 4       : input test cases
        >>> 7
        >>> 10
        >>> 7       : output results
        >>> 44
        >>> 274
    """
    INT_MAX = 10**9 + 9
    T = int(input())
    test_case = [int(input()) for _ in range(T)]

    if max(test_case) < 4:
        for case in test_case:
            if case < 3:
                print(case)
            else:
                print(case+1)
        return

    result = [0 for _ in range(max(test_case) + 1)]
    result[1], result[2], result[3] = 1, 2, 4

    for i in range(4, max(test_case)+1):
        result[i] = (result[i-1] + result[i-2] + result[i-3]) % INT_MAX
        
    for case in test_case:
        print(result[case])

solution()
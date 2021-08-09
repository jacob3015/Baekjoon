"""B 9095 1, 2, 3 더하기(Add One Two Three)
Problem:
    정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

Input:
    첫째 줄에 테스트 케이스의 개수 T가 주어진다.
    각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.
    n은 양수이며 11보다 작다.

Output:
    각 테스트 케이스마다 n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
"""

def solution():
    """정수 n을 1, 2, 3의 합으로 나타내는 방법의 수를 구해 출력한다.
    Extra explanation:
        Dynamic programming의 memoization 기법을 활용해 bottom-up 방식으로 결과를 구한다.
        A(n)이 정수 n을 1, 2, 3의 합으로 나타내는 방법의 수라고 할 때,
        A(n)은 A(n-1)에 1을 추가하는 방법의 수 + A(n-2)에 2를 추가하는 방법의 수 + A(n-1)에 3을 추가하는 방법의 수이다.
        따라서, A(n) = A(n-1) + A(n-2) + A(n-3) (1 <= n <= 11, A(1) = 1, A(2) = 2, A(3) = 4)을 만족한다.

    Tips:
        Dynamic programming의 memoization 기법을 활용할 때 현재 구하려는 값과 이전에 구한 값들과의 관계 찾기에 집중하면 좀 더 빨리 문제를 풀 수 있다.
        결과적으로 문제 풀이에 필요한 점화식을 빨리 찾아낼 수록 더 빨리 문제를 풀 수 있다.
    
    Variables:
        T : 테스트 케이스의 개수
        test_case : 테스트 케이스 list
        result : 테스트 케이스 n을 1, 2, 3의 합으로 나타내는 방법의 수
    
    Example:
        >>> 2       : input T
        >>> 4       : input test cases
        >>> 7
        >>> 7       : output results
        >>> 44
    """
    T = int(input())
    test_case = [int(input()) for _ in range(T)]

    result = [0 for _ in range(12)]
    result[1], result[2], result[3] = 1, 2, 4

    for i in range(4, 12):
        result[i] = result[i-1] + result[i-2] + result[i-3]
        
    for case in test_case:
        print(result[case])

solution()
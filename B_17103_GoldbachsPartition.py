"""B 17103 골드바흐 파티션(Goldbach's Partition)
Problem:
    짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다.
    짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자.
    두 소수의 순서만 다른 것은 같은 파티션이다.

Input:
    첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 1 이상 100 이하이다.
    각 테스트 케이스는 한 줄로 이루어져 있고, 정수 N은 2 이상 1,000,000 이하의 짝수이다.

Output:
    각각의 테스트 케이스마다 골드바흐 파티션의 수를 출력한다.
"""
import math

def solution():
    """골드바흐 파티션의 개수를 구해 출력한다.
    Extra explanation:
        에라토스테네스의 체를 이용해 2 이상 max(N) 이하의 소수를 모두 찾는다.
        이때, max(N)은 주어진 테스트 케이스 중 가장 큰 수를 의미한다.
        2 이상 max(N) 이하의 모든 소수를 이용해 골드바흐 파티션을 구한다.
        이때, 두 소수의 순서만 다른 것은 같은 파티션이므로 개수를 셀 때 제외한다.
    
    Variables:
        T : 테스트 케이스의 개수
        test_case : 주어진 테스트 케이스 list
        test_case_max : 주어진 테스트 케이스 중 가장 큰 수
        prime : 에라토스테네스의 체를 이용해 구한 2 이상 test_case_max 이하의 모든 소수 list
        square_root : test_case_max의 제곱근
        result : 골드바흐 파티션의 개수

    Example:
        >>> 5       : input T
        >>> 6       : input test cases
        >>> 8
        >>> 10
        >>> 12
        >>> 100
        >>> 1       : output results
        >>> 1
        >>> 2
        >>> 1
        >>> 6
    """
    T = int(input())
    test_case = [int(input()) for _ in range(T)]
    test_case_max = max(test_case)

    prime = [True for _ in range(test_case_max+1)]
    square_root = int(math.sqrt(test_case_max))

    for i in range(2, square_root+1):
        if prime[i]:
            j = 2
            while i * j < test_case_max + 1:
                prime[i * j] = False
                j += 1
    prime[0] = prime[1] = False

    for case in test_case:
        result = 0
        for i in range(case//2+1):
            if prime[i] and prime[case - i]:
                result += 1
        print(result)

solution()
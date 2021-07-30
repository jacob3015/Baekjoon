"""B 9613 GCD 합(Sum of GCD)
Problem:
    양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.

Input:
    첫째 줄에 테스트 케이스의 개수 t가 주어진다. t는 1 이상 100 이하의 정수이다.
    각 테스트 케이스는 한 줄로 이루어져 있다.
    각 테스트 케이스는 수의 개수 n이 주어지고, 다음에는 n 개의 수가 주어진다.
    입력으로 주어지는 수는 1,000,000 을 넘지 않는다.
    n은 1 이상 100 이하의 정수이다.

Output:
    각 테스트 케이스마다 가능한 모든 쌍의 GCD의 합을 출력한다.
"""
import math

def solution():
    """주어진 테스트 케이스에서 가능한 모든 쌍의 GCD의 합을 구해 출력한다.

    Variables:
        t : 테스트 케이스의 개수
        test_case : 주어진 테스트 케이스 list
        case : 하나의 테스트 케이스
        element_numbers : 테스트 케이스 원소 개수
        result : 테스트 케이스에서 가능한 모든 쌍의 GCD의 합
    
    Example:
        >>> 1               : input t
        >>> 4 10 20 30 40   : input test case
        >>> 70              : output result
    """
    t = int(input())
    test_case = [list(map(int, input().split())) for _ in range(t)]

    for case in test_case:
        case = case[::-1]
        element_numbers = case.pop()
        result = 0

        for i in range(element_numbers):
            for j in range(i+1, element_numbers):
                result += math.gcd(case[i], case[j])

        print(result)

solution()
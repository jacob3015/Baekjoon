"""B 2089 -2진수(Negative Binary)
Problem:
    -2진법은 부호 없는 2진수로 표현이 된다.
    2진법에서는 2^0, 2^1, 2^2이 표현되지만 -2진법에서는 (-2)^0, (-2)^1, (-2)^2 을 표현한다.
    10진수로 1부터 -2진법으로 표현하자면 1, 110, 111, 100, 101, 11010, 11011, 11000, 11001 등이다.
    10진법의 수를 입력 받아서 -2진수를 출력하는 프로그램을 작성하시오.

Input:
    첫 줄에 10진법으로 표현된 수 N이 주어진다.
    -2,000,000,000 <= N <= 2,000,000,000

Output:
    -2진법 수를 출력한다.
"""

def solution():
    """주어진 정수 N 을 (-2)소인수분해를 이용해 (-2)진법으로 변환한 뒤 결과를 출력한다.

    Variables:
        N : 주어진 정수 N
        result : (-2)소인수분해를 이용해 (-2)진법으로 변환한 결과
    
    Example:
        >>> -13     : input N
        >>> 110111  : output result
    """
    N = int(input())

    if N == 0:
        print(N)
        return

    result = []
    
    while N != 0:
        if N % (-2):
            result.append('1')
            N -= 1
        else:
            result.append('0')
        N //= (-2)

    result = ''.join(result[::-1])
    print(result)
    
solution()
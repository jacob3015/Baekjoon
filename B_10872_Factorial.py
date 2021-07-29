"""B 10872 팩토리얼(Factorial)
Problem:
    0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

Input:
    첫째 줄에 정수 N이 주어진다.
    정수 N은 0이상 12 이하이다.

Output:
    첫째 줄에 N!을 출력한다.
"""

def solution():
    """주어진 정수 N!을 구해 출력한다.
    Extra explanation:
        Dynamic programming의 memoization 기법을 활용해 N!을 구해 출력한다.
    
    Variables:
        N : 주어진 정수 N
        factorial : Memoization을 위한 list, 0부터 N까지의 factorial 결과값이 저장된다.

    Example:
        >>> 5       : input N
        >>> 120     : output N!
    """
    N = int(input())
    factorial = [1 for _ in range(N+1)]

    if N == 0:
        print(factorial[N])
    else:
        for i in range(1, N+1):
            factorial[i] = factorial[i-1] * i
        print(factorial[N])

solution()
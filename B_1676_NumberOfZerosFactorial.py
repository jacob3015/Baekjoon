"""B 1676 팩토리얼 0의 개수(Number of Zeros in Factorial)
Problem:
    N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지의 0의 개수를 구하는 프로그램을 작성하시오.

Input:
    첫째 줄에 N이 주어진다.
    N은 0 이상 500 이하의 정수이다.

Output:
    첫째 줄에 구한 0의 개수를 출력한다.
"""

def solution():
    """N!을 구한 뒤 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지의 0의 개수를 구해 출력한다.
    Extra explanation:
        Memoization을 활용해 N!을 구한 뒤, Stack을 활용해 N!의 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지의 0의 개수를 구한다.
    
    Variables:
        N : 주어진 정수 N
        factorial : Memoization 기법으로 N!을 구하기 위한 list
        n_factorial : N!의 뒤에서부터 처리하기 위한 Stack
        zeros : N!의 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지의 0의 개수

    Example:
        >>> 5   : input N
        >>> 1   : output result
    """
    N = int(input())
    factorial = [1 for _ in range(N+1)]

    if N > 0:
        for i in range(1, N+1):
            factorial[i] = factorial[i-1] * i

    n_factorial = list(str(factorial[N]))
    zeros = 0

    while n_factorial:
        if n_factorial.pop() == '0':
            zeros += 1
        else:
            break

    print(zeros)

solution()
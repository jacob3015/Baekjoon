"""B 2745 진법 변환(Base Conversion)
Problem:
    B진법의 수 N이 주어진다.
    이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
    10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다.
    이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

Input:
    첫째 줄에 N과 B가 주어진다.
    B진법의 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.
    B는 2 이상 36 이하의 자연수이다.

Output:
    첫째 줄에 B진법의 수 N을 10진법으로 변환해 출력한다.
"""
import string

def solution():
    """B진법의 수 N을 10진법으로 변환해 출력한다.

    Variables:
        N : 주어진 B진법의 수 N
        base : 주어진 N의 base(B)
        conversion : 상수 0 ~ 9, A(10) ~ Z(35) 값을 저장한 list
        result : B진법의 수 N을 10진법으로 변환한 결과
    
    Example:
        >>> ZZZZZ 36    : input N, base
        >>> 60466175    : output result
    """
    N, base = map(str, input().split())
    N = list(N)[::-1]
    base = int(base)
    conversion = [str(i) for i in range(10)] + list(string.ascii_uppercase)

    result = 0
    for i in range(len(N)):
        value = conversion.index(N[i])
        result += value * base**i

    print(result)

solution()
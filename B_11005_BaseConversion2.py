"""B 11005 진법 변환 2(Base Conversion 2)
Problem:
    10진법 수 N이 주어진다.
    이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.
    10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다.
    이런 경우에는 알파벳 대문자를 사용한다.

Input:
    첫째 줄에 N과 B가 주어진다.
    N은 10억보다 작거나 같은 자연수이며, B는 2 이상 36 이하의 자연수이다.

Output:
    첫째 줄에 10진법 수 N을 B진법으로 출력한다.
"""
import string

def solution():
    """10진법의 수 N을 B진법의 수로 변환해 출력한다.

    Variables:
        N : 주어진 10진법의 자연수 N
        B : 주어진 B진법의 자연수 B
        conversion : 10진법이 B진법으로 변환되는 값 list
        result : 10진법의 자연수 N을 B진법으로 변환한 결과
    
    Example:
        >>> 60466175 36     : input N, B
        >>> ZZZZZ           : output result
    """
    N, B = map(int, input().split())
    conversion = [str(i) for i in range(10)] + list(string.ascii_uppercase)
    result = ''

    while N:
        result += conversion[N % B]
        N //= B

    print(result[::-1])

solution()
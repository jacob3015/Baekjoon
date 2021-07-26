"""B 10824 네 수(Four Number)
Problem:
    네 자연수 A, B, C, D가 주어진다.
    이때, A와 B를 붙인 수와 C와 D를 붙인 수의 합을 구하는 프로그램을 작성하시오.
    두 수 A와 B를 합치는 것은 A의 뒤에 B를 붙이는 것을 의미한다.

Input:
    첫째 줄에 네 자연수 A, B, C, D가 주어진다.
    A, B, C, D는 1 이상 1,000,000 이하의 자연수이다.

Output:
    A와 B를 붙인 수와 C와 D를 붙인 수의 합을 출력한다.
"""

def solution():
    """주어진 A, B, C, D 자연수에서 A와 B를 붙인 수와 C와 D를 붙인 수의 합을 구해 출력한다.

    Variables:
        A, B, C, D : 주어진 4개의 자연수
    
    Example:
        >>> 10 20 30 40 : input A, B, C, D
        >>> 4060        : output result
    """
    A, B, C, D = map(str, input().split())
    print(int(A+B) + int(C+D))

solution()
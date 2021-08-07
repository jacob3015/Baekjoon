"""B 11576 Base Conversion
Problem:
    타임머신을 개발하는 정이는 오랜 노력 끝에 타임머신을 개발하는데 성공하였다.
    미래가 궁금한 정이는 자신이 개발한 타임머신을 이용하여 500년 후의 세계로 여행을 떠나게 되었다.
    500년 후의 세계에서도 프로그래밍을 하고 싶었던 정이는 백준 사이트에 접속하여 문제를 풀기로 하였다.
    그러나 미래세계는 A진법을 사용하고 있었고, B진법을 사용하던 정이는 문제를 풀 수 없었다.
    뛰어난 프로그래머였던 정이는 A진법으로 나타낸 숫자를 B진법으로 변환시켜주는 프로그램을 작성하기로 하였다.
    N진법이란, 한 자리에서 숫자를 표현할 때 쓸 수 있는 숫자의 가짓수가 N이라는 뜻이다.

Input:
    입력의 첫 줄에는 미래세계에서 사용하는 진법 A와 정이가 사용하는 진법 B가 공백을 구분으로 주어진다.
    A와 B는 모두 2 이상 30 이하의 자연수다.
    입력의 두 번째 줄에는 A진법으로 나타낸 숫자의 자리수의 개수 m이 주어진다. m은 1 이상 25 이하이다.
    세 번째 줄에는 A진법을 이루고 있는 숫자 m개가 공백을 구분으로 높은 자릿수부터 차례대로 주어진다.
    각 숫자는 0 이상 A 미만임이 보장된다. 또한, 수가 0 으로 시작하는 경우는 존재하지 않는다.
    A진법으로 나타낸 수를 10진법으로 변환하였을 때의 값은 양의 정수이며 2^20보다 작다.

Output:
    입력으로 주어진 A진법으로 나타낸 수를 B진법으로 변환하여 출력한다.
"""

def solution():
    """주어진 A진법의 수를 B진법의 수로 변환해 높은 자릿수부터 차례대로 출력한다.

    Variables:
        base_future : 500년 후 미래에서 사용하는 base A
        base_past : 원래 사용했던 base B
        digit_number : A진법 수의 자릿수 개수
        digits : A진법 수의 각 자릿수
        future_to_decimal : A진법에서 10진법으로 변환한 수
        decimal_to_past : 10진법에서 B진법으로 변환한 수
    
    Example:
        >>> 17 8    : input base A, base B
        >>> 2       : input digit number
        >>> 2 16    : input digits
        >>> 6 2     : output result
    """
    base_future, base_past = map(int, input().split())
    digit_number = int(input())
    digits = list(map(int, input().split()))[::-1]

    future_to_decimal = 0
    for i in range(digit_number):
        future_to_decimal += digits[i] * base_future**i

    decimal_to_past = []
    while future_to_decimal:
        decimal_to_past.append(future_to_decimal % base_past)
        future_to_decimal //= base_past

    for num in decimal_to_past[::-1]:
        print(num, end=' ')

solution()
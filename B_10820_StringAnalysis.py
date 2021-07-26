"""B 10820 문자열 분석(String Analysis)
Problem:
    문자열 N개가 주어진다. 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.
    각 문자열은 알파벳 소문자, 대문자, 숫자, 공백으로만 이루어져 있다.

Input:
    첫째 줄부터 N번째 줄까지 문자열이 주어진다.
    문자열의 길이는 100을 넘지 않는다.

Output:
    첫째 줄부터 N번째 줄까지 각각의 문자열에 대해서 소문자, 대문자, 숫자, 공백의 개수를 공백으로 구분해 출력한다.
"""
import sys

def solution():
    """주어진 문자열의 소문자, 대문자, 숫자, 공백의 개수를 구해 출력한다.
    Extra explanation:
        입력되는 문자열의 개수를 알 수 없기 때문에 while문을 사용한다.
        문자열의 끝에 위치한 '\n'을 기준으로 공백의 개수를 구한다.
    
    Variables:
        string : 주어진 문자열 list
        result : 주어진 문자열의 소문자, 대문자, 숫자, 공백의 개수 list
        line : 입력되는 한 줄의 문자열
        lower : 소문자의 개수
        upper : 대문자의 개수
        num : 숫자의 개수
        sapce : 공백의 개수
    
    Example:
        >>> This is String  : input string
        >>> 10 2 0 2        : input result
    """
    string = []
    result = []

    while True:
        line = sys.stdin.readline()
        if len(line) > 2:
            string.append(line)
        else:
            break

    for str in string:
        lower = upper = num = space = 0
        for s in str:
            if s == '\n':
                break
            elif s.islower():
                lower += 1
            elif s.isupper():
                upper += 1
            elif s.isspace():
                space += 1
            else:
                num += 1
        result.append([lower, upper, num, space])

    for res in result:
        print(f'{res[0]} {res[1]} {res[2]} {res[3]}')

solution()
"""B 11655 ROT13
Problem:
    ROT13은 카이사르 암호의 일종으로 영어 알파벳을 13글자씩 밀어서 만든다.
    ROT13은 알파벳 대문자와 소문자에만 적용할 수 있다. 알바벳이 아닌 글자는 원래 글자 그대로 남아 있어야 한다.
    문자열이 주어졌을 때, ROT13으로 암호화한 다음 출력하는 프로그램을 작성하시오.

Input:
    첫째 줄에 알파벳 대문자, 소문자, 공백, 숫자로만 이루어진 문자열 S가 주어진다.
    S의 길이는 100을 넘지 않는다.

Output:
    첫째 줄에 S를 ROT13으로 암호화한 내용을 출력한다.
"""
import string

def solution():
    """주어진 문자열을 ROT13으로 암호화한 뒤 결과를 출력한다.
    Extra explanation:
        String module의 ascii_uppercase와 ascii_lowercase를 활용해 대문자 알파벳 list와 소문자 알파벳 list를 구현한다.
        주어진 문자열의 문자에 맞게 ROT13으로 암화화 한다.
    
    Variables:
        string : 주어진 문자열
        upper : 대문자 알파벳 list
        lower : 소문자 알파벳 list
        result : ROT13으로 암호화한 문자열
    
    Example:
        >>> Baekjoon Problem 11655  : input string
        >>> Onrxwbba Ceboyrz 11655  : output result
    """
    input_string = input()
    upper = list(string.ascii_uppercase) * 2
    lower = list(string.ascii_lowercase) * 2
    result = ''

    for str in input_string:
        if str.isupper():
            result += upper[ord(str) - 65 + 13]
        elif str.islower():
            result += lower[ord(str) - 97 + 13]
        else:
            result += str
            
    print(result)

solution()
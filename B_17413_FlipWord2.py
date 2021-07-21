"""B 17413 단어 뒤집기2(Flip Word 2)
Problem:
    문자열 S가 주어졌을 때, 이 문자열에서 단어만 뒤집으려고 한다.
    먼저 문자열 S는 아래와 같은 규칙을 지킨다.
    1. 알파벳 소문자, 숫자(0~9), 공백, 특수문자(<, >)로만 이루어져 있다.
    2. 문자열의 시작과 끝은 공백이 아니다.
    3. '<'와 '>'가 문자열에 있는 경우 번갈아 가면서 등장하며, '<'이 먼저 등장한다. 또, 두 문자의 개수는 같다.
    태그는 '<'로 시작해서 '>'로 끝나는 길이가 3 이상인 부분 문자열이고, '<'와 '>'사이에는 알파벳 소문자와 공백만 있다.
    단어는 알파벳 소문자와 숫자로 이루어진 부분 문자열이고, 연속하는 두 단어는 공백 하나로 구분된다.
    태그는 단어가 아니며, 태그와 단어 사이에는 공백이 없다.

Input:
    첫째 줄에 문자열 S가 주어진다. S의 길이는 100,000 이하이다.

Output:
    첫째 줄에 문자열 S의 단어를 뒤집어서 출력한다.
"""

def solution():
    """주어진 문자열에서 <tag>를 제외한 단어들만 뒤집어 출력한다.
    Extra explanation:
        '<'와 '>' 내부 문자열은 tag에 해당하며, 그 외 문자열은 tag가 아니다.
        따라서, '<'와 '>' 내부 문자열은 그대로 결과 문자열에 추가하며, 그 외 tag가 아닌 문자열만 뒤집어 결과 문자열에 추가한다.

    Variables:
        S : 주어진 문자열 S
        tag : 주어진 문자열이 tag 인지 확인하기 위한 boolean type variable
        string : 주어진 문자열을 뒤집거나 그대로 결과 문자열에 추가하기 위한 string type variable
        result : 출력되는 결과 문자열
        s : 문자열 S의 부분 문자

    Example:
        >>> <open>tag<close>    : input S
        >>> <open>gat<close>    : output result
    """
    S = input()
    tag = False
    string = result = ''

    for s in S:
        if s == '<':
            tag = True
            if string:
                result += string[::-1]
                string = ''
            string += s
            continue
        if s == '>':
            tag = False
            result += (string + s)
            string = ''
            continue
        if not tag:
            if s == ' ':
                result += (string[::-1] + s)
                string = ''
            else:
                string += s
        else:
            if s == ' ':
                result += (string + s)
                string = ''
            else:
                string += s

    if string:
        result += string[::-1]

    print(result)

solution()
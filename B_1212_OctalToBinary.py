"""B 1212 8진수 2진수(Octal to Binary)
Problem:
    8진수가 주어졌을 때, 2진수로 변환하는 프로그램을 작성하시오.

Input:
    첫째 줄에 8진수가 주어진다. 주어지는 수의 길이는 333,334을 넘지 않는다.

Output:
    첫째 줄에 주어진 수를 2진수로 변환하여 출력한다. 수가 0인 경우를 제외하고는 반드시 1로 시작해야 한다.
"""

def solution():
    """8진수를 10진수로 변환한 뒤, 10진수를 2진수로 변환해 출력한다.
    Extra explanation:
        Python에서 8진수는 '0o' 접두어를 붙혀 표현하므로 주어진 8진수 String에 접두어 '0o'를 붙힌다.
        int() method에 base를 8진수로 넘겨주며 8진수를 10진수로 변환한다.
        format() method에 formatting type을 'b'(binary) 2진수로 넘겨주며 10진수를 2진수 String으로 변환한다.

    Variables:
        octal : 주어진 8진수

    Example:
        >>> 314
        >>> 11001100
    """
    octal = input()
    octal = '0o' + octal
    print(format(int(octal, 8), 'b'))

solution()
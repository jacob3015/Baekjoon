"""B 1373 2진수 8진수(Binary to Octal)
Problem:
    2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.

Input:
    첫째 줄에 2진수가 주어진다. 주어지는 수의 길이는 1,000,000을 넘지 않는다.

Output:
    첫째 줄에 주어진 수를 8진수로 변환하여 출력한다.
"""

def solution():
    """주어진 2진수를 10진수로 변환 후, 10진수를 8진수로 변환하여 출력한다.
    Extra explanation:
        Python에서 2진수는 접두어로 '0b'를 붙여 표현하므로 주어진 2진수를 String으로 입력 받아 '0b'를 접두어로 붙여준다.
        int() method에 base를 2진수로 넘겨주며 2진수를 10진수로 변환한다.
        format() method에 formatting type을 'o'(Octal) 8진수로 넘겨주며 10진수를 접두어를 제외한 8진수 String으로 변환한다.
    
    Variables:
        binary : 주어진 2진수

    Example:
        >>> 11001100    : input binary number
        >>> 314         : output octal number
    """
    binary = input()
    binary = '0b' + binary
    print(format(int(binary, 2), 'o'))

solution()
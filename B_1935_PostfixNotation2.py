"""B 1935 후위 표기식2(Postfix Notation 2)
Problem:
    후위 표기식과 각 피연산자에 대응하는 값들이 주어져 있을 때, 그 식을 계산하는 프로그램을 작성하시오.

Input:
    첫째 줄에 피연산자의 개수(1 <= N <= 26)가 주어진다.
    둘째 줄에는 후위 표기식이 주어진다.
    셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다.
    후위 표기식에서 피연산자는 A~Z의 영대문자이며, A부터 순서대로 사용된다.
    피연산자의 길이는 100을 넘지 않는다.
    피연산자에 대응하는 값은 정수이다.

Output:
    계산 결과를 소수점 둘째 자리까지 출력한다.
"""

def solution():
    """주어진 후위 표기식으로 연산을 수행한 결과를 소수점 둘째 자리까지 출력한다.
    Extra explanation:
        후위 표기식의 연산은 Stack을 활용해 수행할 수 있다.
        후위 표기식을 앞에서부터 완전 탐색하며, 피연산자는 Stack에 push한다.
        연산자가 등장하면 Stack에서 2개의 피연산자를 pop한 뒤 연산을 수행한다.
        이때, 연산을 수행하는 피연산자의 순서는 먼저 pop한 피연산자가 연산자의 뒤(오른쪽)에 위치해야 한다.
        연산 수행의 결과는 다시 Stack에 push한다.
        이 과정을 후위 표기식의 끝까지 반복하며, 마지막에 Stack에 남아있는 값이 연산 수행의 결과가 된다.
        소수점 둘째 자리까지의 출력은 Python의 f-string을 활용한다.
        예) print(f'{variable:.2f}')
    
    Variables:
        N : 피연산자의 개수
        notation : 후위 표기식
        operand : 피연산자
        stack : 후위 연산 수행을 위한 Stack

    Example:
        >>> 5           : input N
        >>> ABC*+DE/-   : input notation
        >>> 1           : input operands
        >>> 2
        >>> 3
        >>> 4
        >>> 5
        >>> 6.20        : output result
    """
    N = int(input())
    notation = input()
    operand = [int(input()) for _ in range(N)]
    stack = []

    for n in notation:
        if 65 <= ord(n) <= 90:
            stack.append(operand[ord(n)-65])
        else:
            a = stack.pop()
            b = stack.pop()
            if n == '+':
                stack.append(b+a)
            elif n == '-':
                stack.append(b-a)
            elif n == '*':
                stack.append(b*a)
            else:
                stack.append(b/a)

    print(f'{stack.pop():.2f}')

solution()
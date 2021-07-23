"""B 1918 후위 표기식(Postfix Notation)
Problem:
    후위 표기법은 연산자가 피연산자 뒤에 위치하는 방법이다.
    중위 표기식을 후위 표기식으로 바꾸는 방법을 간단히 설명하면 이렇다.
    주어진 중위 표기식의 괄호 안의 연산자를 괄호의 오른쪽으로 옮겨주면 된다.
    중위 표기식이 주어졌을 때 후위 표기식으로 고치는 프로그램을 작성하시오.

Input:
    첫째 줄에 중위 표기식이 주어진다.
    단 이 수식의 피연산자는 A~Z의 문자로 이루어지며 수식에서 한 번씩만 등장한다.
    그리고 '-A'와 같이 '-'가 가장 앞에 오거니 'AB'와 같이 '*'가 생략되는 등의 수식은 주어지지 않는다.
    표기식은 알파벳 대문자와 +, -, *, /, (, ) 로만 이루어져 있으며, 길이는 100을 넘지 않는다.

Output:
    첫째 줄에 후위 표기식으로 바뀐 식을 출력하시오.
"""

def solution():
    """주어진 중위 표기식을 후위 표기식으로 바꾼 결과를 출력한다.
    Extra explanation:
        주어진 중위 표기식을 완전 탐색하며 아래 방법에 따라 연산자와 피연산자를 출력할 결과에 추가한다.
        피연산자는 바로 결과에 추가한다.
        연산자는 우선순위를 고려해 Stack에 push 해야 한다.
        연산자의 우선 순위는 아래와 같다. 수가 클 수록 우선 순위가 높다.
        '(' : 0, '+' : 1, '-' : 1, '*' : 2, '/' : 2
        '(' 연산자는 우선 순위가 가장 낮기 때문에 Stack에 push 한다.
        Stack의 top에 위치한 연산자의 우선 순위가 Stack에 push 하려는 연산자의 우선 순위보다 크거나 같을 경우,
        후자의 우선 순위가 더 커질 때 또는 Stack에 더 이상 남아있는 연산자가 없을 때까지 Stack에서 연산자를 pop해 결과에 추가한다.
        이후 Stack에 연산자를 push 한다.
        중위 표기식의 완전 탐색 후 Stack에 남아있는 연산자가 있는 경우 남아 있는 모든 연산자를 결과에 추가한다.
        결과를 출력한다.
    
    Variables:
        infix_notation : 주어진 중위 표기식
        priority : 연산자들의 우선 순위
        operator : 연산자들을 우선 순위에 따라 처리하고 중위 표기식을 후위 표기식으로 바꾸기 위한 Stack
        result : 후위 표기식
    
    Example:
        >>> (A+(B*C))-(D/E) : input infix notation
        >>> ABC*+DE/-       : output postfix notation
    """
    infix_notation = input()
    priority = {'(' : 0, '+' : 1, '-' : 1, '*' : 2, '/' : 2}
    operator = []
    result = ''

    for notation in infix_notation:
        if notation.isalpha():
            result += notation
        else:
            if notation == ')':
                while operator[-1] != '(':
                    result += operator.pop()
                operator.pop()
            elif notation == '(':
                operator.append(notation)
            else:
                while operator and priority[operator[-1]] >= priority[notation]:
                    result += operator.pop()
                operator.append(notation)

    while operator:
        result += operator.pop()
    print(result)

solution()
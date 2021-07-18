"""Problem : B 9012 괄호(Parenthesis)

괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 '(' 와 ')' 만으로 구성되어 있는 문자열이다.
그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
한 쌍의 괄호 기호로 된 '()' 문자열은 기본 VPS 이라고 부른다.
만일 x가 VPS라면 이것을 하나의 괄호에 넣은 새로운 문자열 '(x)'도 VPS가 된다.
그리고 두 VPS x와 y를 접합(concatenation) 시킨 새로운 문자열 xy도 VPS가 된다.
입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.

입력 데이터는 표준 입력으로 사용한다. 입력은 T개의 테스트 데이터로 주어진다.
입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다.
각 테스트 데이터의 첫 째줄에는 괄호 문자열이 한 줄에 주어진다.
하나의 괄호 문자열의 길이는 2 이상 50 이하이다.

출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열이면 'YES', 아니면 'NO'를 한 줄에 하나씩 차례대로 출력해야 한다.
"""

def solution():
    """주어진 괄호 문자열이 VPS면 'YES'를, 아니면 'NO'를 출력한다.
    Extra explanation:
        Stack을 활용해 VPS가 맞는지 확인한다.
    
    Variables:
        T : 테스트 케이스의 개수
        test_case : 주어진 테스트 케이스 list
        stack : 주어진 괄호 문자열이 VPS인지 확인하기 위한 stack

    Example:
        >>> 2               : input T
        >>> (())())         : input test case 1
        >>> (()())((()))    : input test case 2
        >>> NO              : output test case 1 result
        >>> YES             : output test case 2 result
    """
    T = int(input())
    test_case = [input() for _ in range(T)]

    for ps in test_case:
        stack = []
        for p in ps:
            if not stack:
                stack.append(p)
            else:
                if stack[-1] == '(' and p == ')':
                    stack.pop()
                else:
                    stack.append(p)     
        if not stack:
            print('YES')
        else:
            print('NO')

solution()
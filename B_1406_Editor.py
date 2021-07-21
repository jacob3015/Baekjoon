"""B 1406 에디터(Editor)
Problem:
    한 줄로 된 간단한 에디터를 구현하려고 한다.
    이 편집기는 영어 소문자만을 기록할 수 있는 편집기로, 최대 600,000글자까지 입력할 수 있다.
    이 편집기에는 '커서'라는 것이 있는데, 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽), 문장의 맨 뒤(마지막 문자의 오른쪽), 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다.
    즉, 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.
    이 편집기가 지원하는 명령어는 다음과 같다.

    1. L : 커서를 왼쪽으로 한 칸 옮김(커서가 문장의 맨 앞이면 무시됨)
    2. D : 커서를 오른쪽으로 한 칸 옮김(커서가 문장의 맨 뒤이면 무시됨)
    3. B : 커서 왼쪽에 있는 문자를 삭제함(커서가 문장의 맨 앞이면 무시됨)
    4. P $ : $라는 문자를 커서 왼쪽에 추가함

    초기에 편집기에 입력되어 있는 문자열이 주어지고, 그 이후 명령어가 차례로 주어졌을 때,
    모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램을 작성하시오.
    단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.

Input:
    첫째 줄에는 초기에 편집기에 입력되어 있는 문자열이 주어진다.
    이 문자열은 길이가 N이고, 영어 소문자로만 이루어져 있으며, 길이는 100,000을 넘지 않는다.
    둘째 줄에는 입력할 명령어의 개수를 나타내는 정수 M(1 <= M <= 500,000)이 주어진다.
    셋째 줄부터 M개의 줄에 걸쳐 입력할 명령어가 순서대로 주어진다.
    명령어는 위의 네 가지 중 하나의 형태로만 주어진다.

Output:
    첫째 줄에 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 출력한다.
"""
import sys
from collections import deque

def solution():
    """주어진 문장과 명령어를 수행한 뒤 결과를 출력한다.
    Extra explanation:
        커서를 기준으로 문장을 왼쪽 문자열과 오른쪽 문자열로 분리한다면, 명령어 수행 전 왼쪽 문자열이 문장이 되며 오른쪽 문자열은 비어있게 된다.
        명렁어 L 수행 시 왼쪽 문자열의 마지막 문자를 오른쪽 문자열의 첫 문자로 삽입한다.
        명렁어 D 수행 시 오른쪽 문자열의 첫 문자를 왼쪽 문자열의 마지막 문자로 삽입한다.
        명렁어 B 수행 시 왼쪽 문자열의 마지막 문자를 삭제한다.
        명령어 P $ 수행 시 왼쪽 문자열의 마지막 문자로 $를 삽입한다.
        시간 제한을 만족하기 위해 input() method가 아닌 sys.stdin.readline() method를 활용한다.
        Queue를 사용하기 위해 Python의 deque 자료형을 활용한다.
    
    Variables:
        left : 왼쪽 문자열
        right : 오른쪽 문자열
        M : 명령어의 개수
        commands : 주어진 명렁어 list
        string : 모든 명렁어 수행 후의 문장
    
    Example:
        >>> abcd    : input string
        >>> 5       : input M
        >>> P x     : input commands
        >>> L
        >>> B
        >>> D
        >>> P y
        >>> abcxy   : output
    """
    left = deque(sys.stdin.readline().rstrip())
    right = deque()
    M = int(sys.stdin.readline().rstrip())
    commands = [sys.stdin.readline().rstrip() for _ in range(M)]

    for comm in commands:
        if comm == 'L':
            if left:
                right.appendleft(left.pop())
        elif comm == 'D':
            if right:
                left.append(right.popleft())
        elif comm == 'B':
            if left:
                left.pop()
        else:
            left.append(comm[2])
    
    string = left + right
    for s in string:
        print(s, end='')
    print('')

solution()
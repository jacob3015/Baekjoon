"""B 10809 알파벳 찾기(Find Alphabet)
Problem:
    알파벳 소문자로만 이루어진 단어 S가 주어진다.
    각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

Input:
    첫째 줄에 단어 S가 주어진다.
    단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

Output:
    각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ..., z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
    만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다.
    단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.
"""

def solution():
    """주어진 단어 S의 알파벳이 처음 등장하는 위치를 출력한다. 등장하지 않는 경우 -1을 출력한다.
    Extra explanation:
        Counter sort를 활용해 주어진 단어 S의 알파벳이 처음 등장하는 위치를 구해 출력한다.
    
    Variables:
        S : 주어진 단어
        alphabet : 주어진 단어 S의 알파벳이 처음 등장하는 위치 list
    
    Example:
        >>> baekjoon                                                                : input S
        >>> 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1  : output alphabet list
    """
    S = input()
    alphabet = [-1 for _ in range(26)]

    for index in range(len(S)):
        if alphabet[ord(S[index])-97] < 0:
            alphabet[ord(S[index])-97] = index
            
    for alpha in alphabet:
        print(alpha, end=' ')

solution()
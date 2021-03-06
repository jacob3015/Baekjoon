"""B 10808 알파벳 개수(Number of Alphabet)
Problem:
    알파벳 소문자로만 이루어진 단어 S가 주어진다.
    각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.

Input:
    첫째 줄에 단어 S가 주어진다.
    단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

Output:
    단어에 포함되어 있는 a의 개수, b의 개수, ..., z의 개수를 공백으로 구분해서 출력한다.
"""

def solution():
    """주어진 단어 S에 포함된 알파벳 소문자의 개수를 구해 출력한다.
    Extra explanation:
        Counter sort를 활용해 주어진 단어에 포함된 알파벳 소문자의 개수를 구한다.

    Variables:
        S : 주어진 단어
        alphabet : 알파벳 소문자의 개수 list
    
    Example:
        >>> baekjoon                                            : input S
        >>> 1 1 0 0 1 0 0 0 0 1 1 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0 : output result
    """
    S = input()
    alphabet = [0 for _ in range(26)]

    for s in S:
        alphabet[ord(s)-97] += 1
        
    for alpha in alphabet:
        print(alpha, end=' ')

solution()
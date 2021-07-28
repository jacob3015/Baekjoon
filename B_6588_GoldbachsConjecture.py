"""B 6588 골드바흐의 추측(Goldbach's Conjecture)
Problem:
    1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.
    4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
    이 추측은 아직도 해결되지 않은 문제이다.
    백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.

Input:
    입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다. 테스트 케이스의 개수는 100,000개를 넘지 않는다.
    각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다.
    백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.

Output:
    각 테스트 케이스에 대해서, n = a + b 형태로 출력한다.
    이때, a와 b는 홀수 소수이다. 숫자와 연산자는 공백 하나로 구분되어져 있다.
    만약, n을 만들 수 있는 방법이 여러가지라면, b-a가 가장 큰 것을 출력한다.
    또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는 "Goldbach's conjecture is wrong."을 출력한다.
"""
import math

def solution():
    """주어진 수에 대해 골드바흐의 추측을 검증한 뒤 주어진 수를 홀수 소수의 합의 형태로 출력한다.
    Extra explanation:
        에라토스테네스의 체 알고리즘을 활용해 1,000,000 이하의 모든 소수를 구한다.
        에라토스테네스의 체 알고리즘은 2 이상 N 이하의 자연수에 대해 소수의 배수는 소수가 아니라는 것을 이용해 2 이상 N 이하의 모든 소수를 구하는 알고리즘이다.
        이때, 약수 n(2 <= n <= int(math.sqrt(N)))의 배수를 2 이상 N 이하의 자연수에서 제외하면 2 이상 N 이하의 소수를 모두 구할 수 있다.

    Variables:
        INT_MAX : 1,000,000
        prime : 2 이상 1,000,000 이하의 소수 list
        base : 약수 n(2 <= n <= int(math.sqrt(INT_MAX)))
        test_case : 주어진 수 list
        iswrong : 골드바흐의 추측에 부합하는지 확인하는 boolean type variable
    
    Example:
        >>> 42          : input test case
        >>> 0
        >>> 42 = 5 + 37 : output result
    """
    INT_MAX = 1000000
    prime = [i for i in range(INT_MAX+1)]
    base = int(math.sqrt(INT_MAX))
    for i in range(2, base+1):
        if prime[i]:
            j = 2
            while i * j < INT_MAX + 1:
                prime[i * j] = -1
                j += 1
    prime[0] = prime[1] = -1

    test_case = []
    while True:
        number = int(input())
        if number == 0:
            break
        test_case.append(number)
    
    for case in test_case:
        iswrong = True
        for i in range(3, case):
            if prime[i] > 0 and prime[case-prime[i]] > 0:
                print(f'{case} = {prime[i]} + {prime[case-prime[i]]}')
                iswrong = False
                break
        if iswrong:
            print("Goldbach's conjecture is wrong.")

solution()
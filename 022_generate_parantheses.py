from typing import *


def generateParenthesis(n: int) -> List[str]:
    k = 1
    out = ['()']
    tmp = []
    while k < n:
        for seq in out:
            tmp += list(set([f'({seq})', f'(){seq}', f'{seq}()']))
        k += 1
        out = [*tmp]
    print(tmp)
    return [p for p in set(out) if len(p)//2 == n]


print(generateParenthesis(3))

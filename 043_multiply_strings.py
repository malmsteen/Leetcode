
def multiply(num1: str, num2: str) -> str:
    if num2 == '0' or num1 == '0':
        return "0"

    def multbynum(n1: str, n2: str):
        n1 = list(n1)
        ans = ''
        tmp = 0
        for s in n1[::-1]:
            prod = int(s) * int(n2) + tmp
            ones = prod % 10
            ans = str(ones) + ans
            tmp = prod // 10
        if tmp > 0:
            ans = str(tmp) + ans
        return ans

    lines = []
    for i in range(len(num2)-1, -1, -1):
        prod = multbynum(num1, num2[i])
        lines.append(prod + '0'*(len(num2) - 1 - i))
    m = len(max(lines, key=len))
    print(lines)
    linesWzeros = []
    for l in lines:
        linesWzeros.append('0'*(m-len(l)) + l)
    # linesWzeros = [l[::-1] for l in linesWzeros]
    print(linesWzeros)
    tmp = 0
    total = ''
    for tup in zip(*lines):
        summa = sum([int(num) for num in tup]) + tmp
        total = str(summa % 10) + total
        tmp = summa // 10
    if tmp > 0:
        return str(tmp) + total
    return total


num1 = "123456789"
num2 = "987654321"

print(multiply(num1, num2))

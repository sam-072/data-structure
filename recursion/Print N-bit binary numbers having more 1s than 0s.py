# Code by : Sam._.072

def NBinary(ans, op, one, zero, n):
    if n == one + zero:
        ans.append(op)
        return
    op1, op2 = op, op
    if one<=zero:
        op1+='1'
        NBinary(ans, op1, one+1, zero, n)
    else:
        op1 += '1'
        op2 += '0'
        NBinary(ans, op1, one+1, zero, n)
        NBinary(ans, op2, one, zero+1, n)


if __name__ == '__main__':
    n = int(input())
    ans , op = [], ''
    NBinary(ans, op, 0, 0, n)
    print(ans)

    


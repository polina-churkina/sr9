A = int(input('Введите целое десятичное число: '))
k = 0
def change_numbers(A):
    if (A>0):
        return(A-n + m - m*(10**k) + n*(10**k))
    else:
        return(A + n - m + m*(10**k) - n*(10**k))
if not(A // 10 == 0):
    B = A
    if (A>0):
        n = A % 10
        C = n
        while True:
            B = B // 10
            m = B % 10
            k = k+1
            C = C + m*(10**k)
            if C == A:break
    else:
        B = abs(A)
        D = B
        n = B % 10
        C = n
        while True:
            B = B//10
            m = B % 10
            k = k+1
            C = C + m*(10**k)
            if C == D:break
    if (n % 2 == 0) and (m % 2 == 0):
        A = change_numbers(A) 
else:
    print('Введите число больше 10')
print(A)

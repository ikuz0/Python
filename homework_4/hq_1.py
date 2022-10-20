from decimal import Decimal
import math
'''1 Вычислить число π c заданной точностью d
*Пример:*
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$'''


'''π = 2√3*(1 - (1/3)*(1/3) + (1/5)*(1/3)^2 - (1/7)*(1/3)^3… + 1/((2n + 1)*(-3)^n)…)'''

n = 1000000
pi = Decimal(0)
k = 0
while k < n:
    pi += (Decimal(-1)**k)*(Decimal(factorial(6*k))/((factorial(k)**3)
                                                     * (factorial(3*k))) * (13591409+545140134*k)/(640320**(3*k)))
    k += 1
pi = pi * Decimal(10005).sqrt()/4270934400
pi = pi**(-1)

#num = 2*((3*(1+nu))**0.5)
print(pi)


# x = 0
# for k in range(1, 1000):
#     x = x+4*((-1)**(k+1))/(2*k-1)
# print(x)

# def bbp(n):
#     pi = Decimal(0)
#     k = 0
#     while k < n:
#         pi += (Decimal(1)/(16**k))*((Decimal(4)/(8*k+1))-(Decimal(2)/(8*k+4))-(Decimal(1)/(8*k+5))-(Decimal(1)/(8*k+6)))
#         k += 1
#     return pi

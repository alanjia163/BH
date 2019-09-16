#!/usr/bin/python
# -*- coding: UTF-8 -*-
def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    sum =len(primfac)
    return sum


if __name__ == '__main__':
    t =int(input())
    sum =0
    for i in range(2,t+1):
        sum+=primes(i)
    print(sum)



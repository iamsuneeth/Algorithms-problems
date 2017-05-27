from fractions import gcd

def lcm(a,b):
    return a*b//gcd(a,b)

t = int(raw_input())
while t>0:
    n = int(raw_input())
    karray = map(int,raw_input().split())
    lcm = reduce(lcm,karray)
    print lcm
    t-=1
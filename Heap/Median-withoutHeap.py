import sys


n = int(raw_input().strip())
a = []
a_i = 0
for a_i in xrange(n):
    a_t = int(raw_input().strip())
    a.append(a_t)
    a.sort()
    if a_i%2==0:
        print float(a[(a_i+1)/2])
    else:
        print (a[((a_i+1)-1)/2]+a[((a_i+1)+1)/2])/2.0
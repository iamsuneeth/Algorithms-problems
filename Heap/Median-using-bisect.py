import bisect

listt = []
mid = 0
for i in range(n):
    bisect.insort(listt,a[i])
    if (i+1)%2==0:
        print('{:0.1f}'.format((listt[mid]+listt[mid-1])/2))
    else:
        print('{:0.1f}'.format(listt[mid]))
        mid+=1
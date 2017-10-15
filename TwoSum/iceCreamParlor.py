t = int(input())
while t>0:
    table={}
    m = int(input())
    n = int(input())
    flavs = list(map(int,input().split()))
    for x in range(n):
        if m-flavs[x] in table:
            if(x<table[m-flavs[x]]):
                print(x+1,table[m-flavs[x]]+1)
            else:
                print(table[m-flavs[x]]+1,x+1)
        else:
            table[flavs[x]] = x
    t-=1;
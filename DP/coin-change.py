# recursive simple solution

def coinChange(coins, m, n):
    if n==0:
        return 1
    if n<0:
        return 0
    if m<=0 and n>=1:
        return 0
    return coinChange(coins, m-1,n) + coinChange(coins,m,n-coins[m-1])

# iterative DP solution

def coinChange2(coins,n,m):
    matrix = [[0 for x in range(m)] for y in range(n+1)]

    for i in range(m):
        matrix[0][i] = 1
    
    for i in range(1,n+1):
        for j in range(m):
            includeCoin = excludeCoin = 0
            if i - coins[j]>=0:
                includeCoin = matrix[i-coins[j]][j]
            if j>=1:
                excludeCoin = matrix[i][j-1]
            matrix[i][j] = includeCoin + excludeCoin
    return matrix[n][m-1]


print (coinChange2([2,5,3,6],10,4))
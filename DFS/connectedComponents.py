
def dfs(graph, rows, cols, i, j, visited):
    stack = []
    stack.append([i,j])
    count=0
    while len(stack)>0:
        s = stack.pop()
        i,j=s[0],s[1]
        if visited[i][j]==1:
            continue
        visited[i][j]=1
        count+=1
        if i+1<rows and j+1<cols and graph[i+1][j+1]==1:
            stack.append([i+1,j+1])
        if i-1>=0 and j-1>=0 and graph[i-1][j-1]==1:
            stack.append([i-1,j-1])
        if i+1<rows and j-1>=0 and graph[i+1][j-1]==1:
            stack.append([i+1,j-1])
        if i-1>=0 and j+1<cols and graph[i-1][j+1]==1:
            stack.append([i-1,j+1])
        if i+1<rows and graph[i+1][j]==1:
            stack.append([i+1,j])
        if i-1>=0 and graph[i-1][j]==1:
            stack.append([i-1,j])
        if j+1<cols and graph[i][j+1]==1:
            stack.append([i,j+1])
        if j-1>=cols and graph[i][j-1]==1:
            stack.append([i,j-1])

    return count



rows = int(input())
cols = int(input())
adjMatrix=[]
for i in range(rows):
    adjMatrix.append(list(map(int,input().split())))
visited = [[0 for x in range(cols)] for y in range(rows)]
countList=[]
for i in range(rows):
    for j in range(cols):
        if visited[i][j]==0 and adjMatrix[i][j]==1:
            countList.append(dfs(adjMatrix,rows,cols,i,j,visited))
print(max(countList))

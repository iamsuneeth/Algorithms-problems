def ransom_note(magazine, ransom):
    # for x in ransom:
    #     if x in magazine:
    #         magazine.remove(x)
    #     else:
    #         return False
    hashTable = {}
    for x in magazine:
        if x in hashTable:
            hashTable[x]+=1
        else:
            hashTable[x] = 1
    for x in ransom:
        if x in hashTable:
            if hashTable[x]==0:
                return False
            hashTable[x]-=1
        else:
            return False
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
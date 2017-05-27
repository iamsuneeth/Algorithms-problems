from collections import defaultdict
def number_needed(a, b):
    counter1 = [0]*26
    counter2 = [0]*26

    for x in a:
        counter1[x - 'a']+=1
    for x in b:
        counter2[x - 'a']+=1
    count=0
    for i in xrange(26):
        count+=abs(counter1[i]-counter2[i])
    return count



a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)

def checkMatch(a,b):
    if a == ']' and b =='[':
        return True
    elif a == ')' and b == '(':
        return True
    elif a == '}' and b == '{':
        return True
    else:
        return False

def is_matched(expression):
    stack=[]
    for x in expression:
        if len(stack)!=0:
            if checkMatch(x,stack[-1]):
                stack.pop(-1)
                continue
        stack.append(x)
    return len(stack)==0

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
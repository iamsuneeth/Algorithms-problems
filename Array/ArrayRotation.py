def array_left_rotation(a, n, k):
  while k>0:
    a.append(a.pop(0))
    k-=1
  return a

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))

a,b,c = map(int,input('Введите 3 числа: ').split())
s = []
s.append(a)
for i in range(c-1):
    s.append(s[i]+b)
print(*s)
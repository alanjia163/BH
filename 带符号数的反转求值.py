x = -120
symbol = 1
# if x==0:
# return 0
if x < 0:
    x = -x
    symbol = -1

t = str(x)[::-1]
for i in range(len(t)):
    if t[i] != '0':
        t = t[i:]
        break
x = symbol * int(t)
print(x)
print(type(x))
# return x

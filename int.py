

a = 23
print(type(a))
print(isinstance(a, int))
print(isinstance(a, bool))

b = 0b1101
c = 0o23
d = 0x23

print(a,b,c,d, sep=' ')

# 3.x에서는 int와 long이 합쳐졌다.
e = 2**1024
print(type(e))
print(e)

# 변환 함수
print(oct(38))
print(hex(38))
print(bin(38))
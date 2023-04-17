l = [1,2,3,4,5,6,7,8,9]

# print(l)
# print(l[:2])
# print(l[4:6])
# print(l[::2])
# print(l[::-2])

# a = ['a','b','c']
# n = [1,2,3,4]
# x = [a,n]
# print(x)
# print(x[0][2])
# print(x[1][:])

s = ['a','b','c']
s[0] = 'X'
print(s)
s[1:2] = []
print(s)
s.append('s')
print(s)
s.pop()
print(s)


s = [1,2,2,2,3]
s.remove(2)
print(s)

a = [1,2,3,4,5]
b = [6,7,8,9,10]
x = a+b
print(x)
a += b
print(a)
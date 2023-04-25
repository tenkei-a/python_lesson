# list
# t = (1, 2, 3, 4, 5)
# t2 = (5, 6, 7, 8, 9, 10)

# r = []
# for i in t:
#     r.append(i)
# print(r)

# r = [i for i in t if i % 2 == 0]
# print(r)


# r = []
# for i in t:
#     for j in t2:
#         r.append(i * j)
# print(r)

# r = [i * j for i in t for j in t2]
# print(r)


# dictionary
# w = ['mon', 'tue', 'wed']
# f = ['coffee', 'milk', 'water']

# d = {}
# for x, y in zip(w, f):
#     d[x] = y
# print(d)

# d = {x: y for x, y in zip(w, f)}
# print(d)


# set
# s = set()
# for i in range(10):
#     s.add(i)

# print(s)

# s = {i for i in range(10) if i % 2 == 0}
# print(s)

# generator
def g():
    for i in range(10):
        yield i
g = g()

g = (i for i in range(10) if i % 2 == 0)
# g = tuple(i for i in range(10))
print(type(g))
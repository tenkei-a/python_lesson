# def menu(entree = 'beef', drink = 'wine', dessert = 'ice'):
#     print(entree)
#     print(drink)
#     print(dessert)

# キーワード引数を指定すれば順序は気にしなくてもよい
# menu(entree = 'beef', drink = 'beer', dessert = 'ice')
# menu()


# def test_func(x, l=None):
#     if l is None:
#         l = []
#     l.append(x)
#     return l

# y = [1, 2, 3]
# r = test_func(100, y)
# print(y)

# y = [1, 2, 3]
# r = test_func(200, y)
# print(y)

# r = test_func(100)
# print(r)
# r = test_func(100)
# print(r)

# 位置引数のタプル化
# def say_something(word, *args):
#     print(word)
#     for arg in args:
#         print(arg)

# say_something('hi', 'Mike', 'Nancy')

# t = ('Mike', 'Nancy')
# say_something('Hi!', *t)

# キーワード引数の辞書化
def menu(food, *args, **kwargs):
    # print(**kwargs)
    for k,v in kwargs.items():
        print(k, v)

menu('banana', 'apple', 'orange', entree = 'beef', drink = 'coffee')
# menu(entree = 'beef', drink = 'coffee')
# d = {
#     'entree' : 'beef',
#     'drink'  : 'ice coffee',
#     'dessert': 'ice'
# }
# menu(**d)




def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('kwargs:', func, kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
    return wrapper

@print_info
@print_more
def add_num(a, b):
    print(a + b)
    return a + b
add_num(10, 20)

# @print_info
# def sub_stract(a, b):
#     print(a - b)
#     return a - b
# sub_stract(10,20)

# f = print_info(add_num)
# r = f(10,20)
# print(r)


# def deco(func):
#     def wrapper(*args, **kwargs):
#         print('--start--')
#         func(*args, **kwargs)
#         print('--end--')
#     return wrapper

# @deco
# def test():
#     print('Hello Decorator')

# test()
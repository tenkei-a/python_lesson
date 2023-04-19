# x = 0

# if x < 0:
#     print('negative')
# elif x == 0:
#     print('zero')
# else:
#     print('positive')


# a = 5
# b = 10

# if a > 0:
#     print('a is positive')
#     if b > 0:
#         print('b ispositive')


# y = [1,2,3]
# x = 1

# if x in y:
#     print('in')

# if 100 not in y:
#     print('not in')

# a = 1
# b = 2

# if a != b:
#     print('Not equal')

# 変数の値が入っているかどうかの確認にも使える
# is_ok = True
# a = 'aaa'
# a = ''
# if a:
#     print('ok!')
# else:
#     print('no!')

# isはnoneの判定をするときをメインとして使用する
is_empty = None
print(is_empty)
print(type(is_empty))

if is_empty is None:
    print('None')

print(1 == True)
print(True is True)
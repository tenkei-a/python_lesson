# l = [1, 2, 3]
# i = 5

# try:
#     l[0]
# except IndexError as ex:
#     print("Don't worry: {}".format(ex))
# except NameError as ex:
#     print(ex)
# except Exception as ex:
#     print('other: {}'.format(ex))
# else:
#     # エラーが起きずに問題なく抜けたときに実行される
#     print('done')
# finally:
#     # 何が起きても動作する
#     print('clean up')


# self
# 自分でエラーを起こすことができる
# raise IndexError('test error')

class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next.')
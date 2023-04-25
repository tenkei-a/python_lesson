# 重複している物を抽出するときに集合は使える
my_friends = {'A','B','C'}
A_friends = {'B','D','E'}

print(my_friends & A_friends)

# ユニークなものを抽出するときに集合は使える
f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)
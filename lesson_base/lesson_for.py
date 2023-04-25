# some_list = [1,2,3,4]
# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1

# iにはsome_list[i]の値が入っている
# for i in some_list:
#     print(i)

# for s in 'abcde':
#     print(s)

# for word in ['My', 'name', 'is', 'Mike']:
#     if word == 'name':
#         # break
#         continue
#     print(word)

# for fruit in ['apple', 'banana', 'orange']:
#     if fruit == 'banana':
#         print('I am not like banana')
#         continue
#     print(fruit)
# else:
#     print('I ate all!')

d = {'x':100, 'y':200}
# print(d.items())
# [('x', 100), ('y', 200)]
# k = 'x', v = 100
for k, v in d.items():
    print(k, ':', v)
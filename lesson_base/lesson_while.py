# count = 0
# while count < 5:
#     print(count)
#     count += 1

# count = 0
# while True:
#     if count >= 5:
#         break

#     if count == 2:
#         count += 1
#         continue
#     print(count)
#     count += 1

# count = 0
# while count < 5:
#     if count == 1:
#         break
#     print(count)
#     count += 1
# # breakで抜けなければ実行する
# else:
#     print('done')

while True:
    # input():入力用の関数
    word = input('Enter:')
    num = int(word)
    if num == 100:
        break
    print('next')
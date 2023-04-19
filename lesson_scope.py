'''
Test Test ###############
'''


animal = 'cat'

def f():
    # print(animal)
    # global animal
    # animal = 'dog'
    # print('local', animal)
    animal = 'dogs'
    # locals: dict型
    print('local:', locals())

f()
# print('global:', animal)
print('global:', globals())
days = ['Mon', 'Tue', 'Wed', 'Thr']
fruites = ['apple', 'banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer', 'coke']

# for i in range(len(days)):
#     print(days[i], fruites[i], drinks[i])

for days, fruites, drinks in zip(days, fruites, drinks):
    print(days, fruites, drinks)
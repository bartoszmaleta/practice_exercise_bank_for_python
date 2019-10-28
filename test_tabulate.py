# from tabulate import tabulate

# data = [[1, 'Liquid', 24, 12], 
#         [2, 'Virtus.pro', 19, 14], 
#         [3, 'PSG.LGD', 15, 19], 
#         [4, 'Team Secret', 10, 20]]
# print(tabulate(data, headers=["Pos", "Team", "Win", "Lose"]))

from tabulate import tabulate
print(tabulate([['Alice', 24], ['Bob', 19]], headers=['Name', 'Age']))

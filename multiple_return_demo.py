x = 1
y = 7
def change_stuff():
    return 1000, 298249824

print(x, y)
# --> 1, 7

x,y = change_stuff()
print(x, y)
# --> 1000, 298249824
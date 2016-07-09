x = 1
y = 7
def change_stuff():
    global x
    x = 1000
    y = 298249824

print(x, y)
# --> 1, 7

change_stuff()
print(x, y)
# --> 1000, 7
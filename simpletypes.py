my_int = 5
my_float = 3.14159
my_bool = True
my_array = [10,20,40,30,2]
my_dict = {"red": (255,0,0), "white": (255,255,255), "green": (0,255,0), "blue": (0,0,255)}

def mod_int(x):
    x = 1000

def mod_array(a):
    a[0] = 1000

mod_int(my_int)
mod_array(my_array)

print(my_int)
print(my_array)
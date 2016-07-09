import time

sum = 0

start = time.time()

for i in range(2200000):
    sum = sum + i
print(sum)

end = time.time()

print("elapsed ", end-start, "seconds")


summ = 0
for i in range(1000, 20001):
    if i % 3 == 0 or i % 5 == 0:
        summ += 1
print(summ)

summ = []
for i in range(1000, 20001):
    if i % 3 == 0 and i % 5 == 0:
       summ.append(i)

print(sum(summ))

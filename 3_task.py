def fibo(zero_step, first_step, threshold):
    next_step = 0
    list_of_numbers = [zero_step, first_step]
    while next_step < threshold:
        next_step = zero_step + first_step
        zero_step = first_step
        first_step = next_step
        if next_step < threshold:
            list_of_numbers.append(next_step)
    return(list_of_numbers)

fibo_list = fibo(1, 1, 10000000)

even_list = []
for number in fibo_list:
    if number % 2 == 0:
        even_list.append(number)

print(len(fibo_list))
print(sum(even_list))
print(even_list)
print(fibo_list[-2])

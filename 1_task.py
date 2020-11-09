def plural_form(value, form1, form2, form3):
    n = abs(value) % 100

    n1 = n % 10

    result_form = form3
    if 10 < n < 20:
        result_form = form3
    elif 1 < n1 < 5:
        result_form = form2
    elif n1 == 1:
        result_form = form1
    else:
        print('Неизвестная ошибка')
    return f'{value} {result_form}'

print(plural_form(1, 'яблоко', 'яблока', 'яблок'))
print(plural_form(2, 'яблоко', 'яблока', 'яблок'))
print(plural_form(11, 'студент', 'студента', 'студентов'))
print(plural_form(15, 'студент', 'студента', 'студентов')) 
print(plural_form(3, 'студент', 'студента', 'студентов')) 

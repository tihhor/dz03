# можно вводить цифры через  любой разделитель из , / ;

my_list1 = input('Введите список 1 через запятую: ').replace('/',',').replace(';',',').split(',')
my_list2 = input('Введите список 2 через запятую: ').replace('/',',').replace(';',',').split(',')

my_set_diff = set(my_list1) - set(my_list2)
print('Результат: ', my_set_diff)

q_list = input('Введите количество элементов списка: ')
my_list =  []

for i in range(int(q_list)):
    my_list.append(input('Введите элемент '+str(i+1)+': '))

my_list.sort()
print(my_list)


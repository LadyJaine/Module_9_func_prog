first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (len(x) - len(y) for x,y in zip(first,second) if len(x) != len(y))
print(list(first_result))
#В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин
# строк из списков first и second, если их
# длины не равны. Для перебора строк попарно из двух списков используйте функцию zip
second_result = (len(first[x]) == len(second[y]) for x in range(len(first)) for y in range(len(second)) if x == y)
print(list(second_result))
#2.В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения
# строк в одинаковых позициях из списков first и second.
# Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.

def is_prime(func):
    def arrogate(*args):
        d = func(*args) #получить результат функции и сохранить ее в переменную
        for x in range(2,d):
            if d % x == 0:
                print('Составное')
                break
        else:
            print('Простое')
    return arrogate


@is_prime
def sum_three(*args):
    result = 0
    for i in args:
        result += i
    print(result)
    return result

result = sum_three(7,8,9,3,5)

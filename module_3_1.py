# Задача "Счётчик вызовов":


calls = 0
def count_calls():
    global calls
    calls += 1



#принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
def string_info(str1):
    count_calls()
    a = len(str1), str1.upper(), str1.lower()

    return a
  
# Функция is_contains принимает два аргумента: строку и список,
# и возвращает True, если строка находится в этом списке,
# False - если отсутствует.
# Регистром строки при проверке пренебречь: UrbaN ~ URBAN.is_contains()


def is_contains(str1 , spis1):
    count_calls()
    bo1 = False
    b = str1.lower()

    for a in spis1:
        c=str(a).lower()

        if b in  c:

            bo1 = True
    return bo1

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
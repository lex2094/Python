# Требуется определить, является ли данный год високосным.
#
# Напомним, что високосными годами считаются те годы, порядковый номер которых либо кратен 4, но при этом не кратен 100, либо кратен 400 (например, 2000-й год являлся високосным, а 2100-й будет невисокосным годом).
#
# Программа должна корректно работать на числах 1900≤n≤3000.

var1 = int(input())


if (var1 % 4 == 0 and not var1 % 100 == 0 or var1 % 400 == 0):
        print("Високосный")
else:
    print("Обычный")


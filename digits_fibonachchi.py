# ПОСЛЕДОВАННОСТЬ ФИБОНАЧИ, КОГДА НОВОЕ ЧИСЛО, ЭТО СУММА ДВУХ ПРЕДЫДУЩИХ

print ('ПЕРВЫЙ СПОСОБ:')
fir, sec, count = 1, 1, 0
while sec < 1000:
    count += 1
    print (sec)
    next_fir = fir + sec
    next_sec = fir
    fir, sec = next_fir, next_sec
print ('Программой пройдено', count, 'чисел')


# МОЖНО ЗАПИСАТЬ ДРУГИМ СПОСОБОМ
print ('\nВТОРОЙ СПОСОБ:')

a, b = 1, 1
while b < 100:
    print (b)
    a, b = b, a + b

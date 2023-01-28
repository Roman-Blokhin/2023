# ПОСЛЕДОВАННОСТЬ ФИБОНАЧИ, КОГДА НОВОЕ ЧИСЛО, ЭТО СУММА ДВУХ ПРЕДЫДУЩИХ

print ('ПЕРВЫЙ СПОСОБ:')
fir, sec = 1, 1
while sec < 1000:
    print (sec)
    next_fir = fir + sec
    next_sec = fir
    fir, sec = next_fir, next_sec

# МОЖНО ЗАПИСАТЬ ДРУГИМ СПОСОБОМ
print ('\nВТОРОЙ СПОСОБ:')

a, b = 1, 1
while b < 100:
    print (b)
    a, b = b, a + b

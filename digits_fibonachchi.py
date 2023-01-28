# ПОСЛЕДОВАННОСТЬ ФИБОНАЧИ, КОГДА НОВОЕ ЧИСЛО, ЭТО СУММА ДВУХ ПРЕДЫДУЩИХ

fir, sec = 1, 1
while sec < 1000:
    print (sec)
    next_fir = fir + sec
    next_sec = fir
    fir, sec = next_fir, next_sec

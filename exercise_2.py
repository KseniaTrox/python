second = int(input("Введите время в секундах "))
h = second // 3600
m = second // 60 % 60
s = second % 60
print( "%.2d"%h, ":" "%.2d"%m, ":" "%.2d"%s ,  sep="")
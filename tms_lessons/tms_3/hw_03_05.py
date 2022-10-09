#Реализовать вычисление факториала с помощью цикла while и for.
n = 5

fac = 1
while n > 1:
    fac *= n
    n -= 1

assert fac == 120

n = 5
fac = 1

for i in range(1, n+1):
    fac *=i
    p
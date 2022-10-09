#Ввести целое число N. Получить сумму кубов всех целых чисел от 1 до N (включая).

#Реализовать через while и for


N=6
su = sum(i*i*i for i in range(1, N))
print(su)

N = 5
sum = 0
i = 1

while i<=N:
    sum=sum+i*i*i
    i+=1
    print(sum)
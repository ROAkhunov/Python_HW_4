#  Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
print('количество элементов первого множества:')
n=int(input())
print('количество элементов второго множества:')
m=int(input())
list1=[]
list2=[]
for i in range(n):
    print('введите элемент первого множества:')
    list1.append(input())
for i in range(m):
    print('введите элемент второго множества:')
    list2.append(input())
# print(list1)
# print(list2)
i=0
j=1
while i < len(list1):
    while j <len(list1):
        if list1[i]<list1[j]:
            j+=1
        else:
            if list1[i]==list1[j]:
                list1.pop(i)
                j+=1
                i-=1
            else:
                list1.insert(i,list1[j])
                list1.pop(j+1)
                j+=1
    i+=1
    j=i+1
# print(list1)
i=0
j=1
while i < len(list2):
    while j <len(list2):
        if list2[i]<list2[j]:
            j+=1
        else:
            if list2[i]==list2[j]:
                list2.pop(i)
                j+=1
                i-=1
            else:
                list2.insert(i,list2[j])
                list2.pop(j+1)
                j+=1
    i+=1
    j=i+1
# print(list2)
set1 = set(list1)
set2 = set(list2)
result= set1.union(set2)    
print (result)
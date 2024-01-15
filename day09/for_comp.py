#for_comp

# a = []
# for i in range(1000):
#     a.append(i)


# a =  [i for i in range(1001)]
# print(a) #0~1000리스트 출력
#
# b =  [i for i in range(101)]
# print(b)
#
# c = [i for i in range(1,501)]
# print(c)
#
# d = [i for i in "megastudy"]
# print(d) #['m', 'e', 'g', 'a', 's', 't', 'u', 'd', 'y']

# e = [i*2 for i in range(1,101)]
# print(e)
#
# f = [i**2 for i in range(1,11)]
# print(f) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# g = [i+5 for i in range(1,11)]
# print(g) #[6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#


# for comp 조건문
# 1. if 가 뒤에서 필터링
# [i for i in range(1,101) if i % 5 ==0]
# fruits = ['apple','orange','mango','melon']
# a = [i for i in fruits if i.count('p')>=1]
# print(a)
# a = [i for i in fruits if i.count('o')==1]
# print(a)
# a = [i for i in fruits if len(i)>=6]
# print(a)

#2. if - else
a = ['🤣' if i%5 ==0 else i for i in range(1,101)]
print(a)

# n입력, 100까지 출력. n배수만 당근 출력
n = int(input("100 이하 정수 입력:"))
b = ['🤣' if i%n ==0 else i for i in range(1,101)]
print(b)

#fruits = ['apple','strawberry','orange','mango','melon']
#5글자 이하면 대문자로 바꿔 출력, 아니면 이모지로 출력
fruits = ['apple','strawberry','orange','mango','melon']
c = [i.upper() if len(i)<=5 else '🤣' for i in fruits]
print(c)


#for comp 중첩 루프문
f = [i*j for i in range(1,4) for j in range(1,4)]
print(f) #[1, 2, 3, 2, 4, 6, 3, 6, 9]
#i - 1일때,  j - 1,2,3
#i - 2일때,  j - 1,2,3
#i - 3일때,  j - 1,2,3

















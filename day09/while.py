#while
#조건식이 없으면 무한 루프에 빠짐

#while이용 첫번째 방법
# a = 1
# while a < 10:
#     print('아메리카노')
#     a +=1
#
# while True:
#     print("너가 숫자 1을 넣어야 탈출 가능")
#     n = int(input("숫자 입력:"))
#     if n ==1:
#         break

#while : 유저가 끝을 결정
#for : 프로그래머가 끝을 결정

list=[]

while True:
    print("메가커피 프로그램")
    print("1.커피 등록하기")
    print("2.커피 메뉴보기")
    print("3.시스템 종료")
    n = int(input("번호 입력:"))
    if n == 1:
        print("커피 등록 시스템")
        c = input("커피 이름 입력:")
        list.append(c)
        print("등록완료")
    elif n == 2:
        if len(list) == 0:
            print("메뉴가 없음")
        else:
            print(list)
    elif n == 3:
        print("이용 감사")
        break
    else:
        print("숫자 재입력")


















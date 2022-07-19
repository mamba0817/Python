
# # 변수선언
# list_test = [1, 2, 1, 2]
# value = 2

# #list_test 내부에 value 가있다면 반복
# while value in list_test:
#     list_test.remove(value)


# print(list_test)

# #시간과 관련된 기능을 가져온다
# import time

# #변수를 선언합니다
# number = 0

# # 5초동안 반복한다
# target_tick = time.time() + 5
# while time.time() < target_tick:
#     number += 1

# #출력한다
# print("5초 동안 {}번 반복했습니다.".format(number))

# #출력합니다
# print("time.time ====> " , time.time())
# print("5초 동안 {}번 반복했습니다.".format(number))


# #변수를 선언합니다.
# i = 0

# #무한 반복합니다.
# while True:
#     #몇번째 반복인지 출력합니다.
#     print ("{}번째 반복문입니다.".format(i))
#     i = i + 1 

#     if i == 5: # i > 4
#         break

#     #반복문을 종료합니다.
#     input_text = input("> 종료하시겠습니까?(y): ")
#     if input_text in ["y", "Y"]:
#         print("반복을 종료합니다.")
#         break 

#변수를 선언합니다
# numbers = [5,15,6,20,7,25]

# #반복을 돌립니다
# for number in numbers:
#     #number가 10보다 작으면 다음 반복으로 넘어갑니다.
#     if number < 10:
#         continue
#     #출력
#     print(number)

# a = range(5)
# print(a)

# print(list(range(10)))


#리스트를 선언하고 뒤집는다
# list_a = [1,2,3,4,5]
# list_reversed = reversed(list_a)

# #출력
# print("# reversed() 함수")
# print("reversed([1,2,3,4,5]):", list_reversed)
# print(next(list_reversed))
# print(next(list_reversed))
# print(next(list_reversed))
# print(next(list_reversed))
# print(next(list_reversed))
# print("list(reversed([1,2,3,4,5])):",list (list_reversed))
# print()

# #반복문 적용
# print("# reversed() 함수와 반복문")
# print("for i in reversed([1,2,3,4,5]):")
# for i in reversed(list_a):
#     print("-", i)

# temp = reversed([1,2,3,4,5,6])
 
# for i in temp:
#     print("첫번째 반복문: {}".format(i))

# for i in temp:
#     print("두 번째 반복문: {}".format(i))


# #변수선언
# example_list = ["요소A , 요소B , 요소 C"]

# #그냥출력
# print("# 단순 출력")
# print(example_list)
# print()

# #enumerate
# print("# enumerate() 함수 적용 출력")
# print(enumerate(example_list))
# print()

# #list() 함수로 강제 변환해 출력합니다.
# print("# list() 함수로 강제 변환 출력")
# print(list(enumerate(example_list)))
# print()

# #for 반복문과 enmerate()함수 조합해서 사용
# print("# 반복문과 조합하기")
# for i, value in enumerate (example_list):
#     print("{}번째 요소는 {}입니다.".format(i, value))

#변수선언
# example_dictionary = {
#     "키A": "값A",
#     "키B": "값B",
#     "키C": "값C",
# }

# # 딕셔너리의 item() 함수 결과 출력하기
# print("# 딕셔너리의 items()함수")
# print("items()", example_dictionary.items())
# print()

# #for 반복문과 items()함수 조합해서 사용
# print("# 딕셔너리의 items() 함수와 반복문 조합하기")

# for key, element in example_dictionary.items():
#     print("dictionary[{}] = {}".format(key, element))

# array = []

# for i in range(0,20,2):
#     array.append(i * i)

# print(array)

# array = [i * i for i in range(0,20,2)]
# print(array)

# array = ["사과", "자두", "초콜릿", "바나나", "체리"]
# output = [fruit for fruit in array if fruit != "초콜릿"]
 
# print(output)




#합에 0을 넣기
#for i 1~101

    #i를 이진수로 변환해서 변수 (a)에 넣기
    #a에서 0의 갯수.(.count) 가 1개인 경우
    #출력, 합에 누적

# for문이 끝나면 합계출력

# total = 0

# for i in range(1,101):
#     binary = "{:b}".format(i)
#     if binary.count("0") == 1:
#         print (i,":",binary)
#         total += i
# print("합계:",total)


# total = 0
# for i in range(0,101):
#     octal = "{:o}".format(i)
#     if octal.count("0") == 1:
#         print(i, ":", octal)
#         total += i
# print(total)

# total = 0
# # print([i for i in range(0, 101) if "{:0}".format(i).count("0") == 1])

# output = [i for i in range(0, 101) if "{:o}".format(i).count("0") == 1]
# # print(ouput)
# for i in output:
#     print("{} : {}".format(i, "{:o}".format(i)))
# print("합계 : ", sum(output))

# def hello03(num):
#     for i in num:
#         print("안녕하세요")
   

# str = "안녕하세요"

# def hello_01(n, str):
#     for i in range(n):
#         print(str)

# hello_01(5, "안녕")

# def print_n_times(n, *values):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()

# print_n_times(6, "배고파", "엄첨", "매우", "몹시", "많이")

# def print_n_times(*values, n=2):
# #n번반복
#     for i in range(n):
#         #values는 리스트처럼 활용한다
#         for value in values:
#             print(value)
#         #단순 줄바꿈
#         print()

# print_n_times("안녕", 3)

# def test(a, *values, b=10, c=100 ):
#     print(a + b + c)
#     for value in values:
#         print(value)

# # # 1)기본형태
# # test(10,20,30)
# # # 2)키워드 매개변수로 모든 매개변수를 지정한 형태
# # test(a=10, b=100, c=200)
# # # 3)키워드 매개변수로 모든 매개변수를 마구잡이로 지정한 형태
# # test(c=10, a=100, b=200)
# # # 4)키워드 매개변수로 일부 매개변수만 지정한 형태
# # test(10, c=200)

# test(10, "즐거운", "파이썬", "프로그래밍",b=50,c=50)

# #함수값
# def return_test():
#     return 100S
#     #함수 호출
# value = return_test()
# print(value)


# #함수의 기본사용
# def sum_all(start=1, end=5):
#     output = 0
#     for i in range(start, end + 1,):
#         output += i
#     return output

# let=int(input("첫번째> "))
# var=int(input("두번째> ")) 

# print(sum_all(let,var))

def mul(*values):
    # output = 1
    for value in values:
        output *= value
    return output


print(mul(5, 7, 9, 10))
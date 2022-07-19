# output_a=int("52")
# output_b=float("52.273")

# print(type(output_a),output_a)
# print(type(output_b), output_b)

# input_a = float(input("실수형 숫자1>"))
# input_b = float(input("실수형 숫자2>"))

# print("덧셈결과 : ", input_a + input_b)
# print("뺼셈결과 : ", input_a - input_b)
# print("곱셈결과 : ", input_a * input_b)
# print("나눗셈결과 : ", input_a / input_b) 

# input_c = int(input("정수형 숫자 >"))60

# string_a="{}만원".format(10)
# print(string_a)
# print(type(string_a))

# format_a="{}만 원".format(5000) 
# format_b="파이썬 열공하여 첫연봉 {}만 원 만들기".format(5000)
# format_c="{} {} {}".format(3000, 4000, 5000)
# format_d="{} {} {}".format(1, "문자열", True)

# print(format_a)
# print(format_b)
# print(format_c)
# print(format_d)

# #정수
# output_a = "{:d}".format(52)
# #특정 칸에 출력하기
# output_b = "{:5d}".format(52)
# output_c = "{:10d}".format(52)


# #빈칸을 0으로 채우기
# output_d = "{:05d}".format(52)
# output_e = "{:05d}".format(-52)

# print("#기본")
# print(output_a)                     
# print("#특정 칸에 출력하기")
# print(output_b)
# print(output_c)
# print("#빈칸을 0으로 채우기")
# print(output_d)
# print(output_e)

# output_a = 52.0
# output_b = "{:g}".format(output_a)
# print(output_a)
# print(output_b)

# a = "HELLO PYTHON pROGRAMMING..."
# # print(a.upper())
# print (a.lower())

# input_a = """
#         안녕하세요 
# 문자열 함수를 알아봅시다"""

# print(input_a)

# input_b = """
#         안녕하세요 
# 문자열 함수를 알아봅시다""" 
# print(input_b.strip())

# print(input_a.isspace())

# a = "10, 20, 30, 40, 50".split("  ")
# print(a)

# string = "hello"

# a =input(">1번째숫자:100")
# b =input(">2번째 숫자:200 ")
# print("{}+{}={}".format())

# x = 20
# under_20 = x < 20
# print("under_20:", under_20)
# print("not under_20:", not under_20)

# #입력을 받습니다
# number = input("정수 입력> ")
# number = int(number)

# #양수 조건
# if number > 0:
#     print("양수입니다")

# #음수 조건
# if number < 0:
#     print("음수입니다")

# #0조건
# if number == 0:
    # print("0 입니다")

#날짜/시간과 관련된 기능을 가져옵니다.
# import datetime

#현재 날짜/시간을 구합니다.
# now = datetime.datetime.now()


#출력합니다
# print(now.year,"년")
# print(now.month, "월")
# print(now.day, "일")
# print(now.hour, "시")
# print(now.minute, "분")
# print(now.second, "초")

# format_a = "{}년 {}월 {}일 {}시 {}분 {}초 오늘은 비가 준나게 온다".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
# print(format_a)

#오전구분
# if now.hour < 12:
#     print("현재 시각은 {}시로 오전입니다!".format(now.hour))

#오후 구분
# if now.hour >= 12:
#     print("현재시각은 {}시로 오후입니다!".format(now.hour))

# import datetime

# now = datetime.datetime.now()

# if 1 <= now.month <= 2 or now.month ==12:
#     print("이번달은 {}월로 겨울입니다".format(now.month))

# if 3<= now.month <=5:
#     print("이번달은 {}월로 봄입니다".format(now.month))

# if 6<= now.month <=8:
#     print("이번달은 {}월로 여름입니다".format(now.month))
    
# if 9<= now.month <=11:
#     print("이번달은 {}월로 가을입니다".format(now.month))


# number = input("정수입력> ")

# last_character = number[-1]
# last_number = int(last_character)

# #짝수확인
# if last_number == 0\
#     or last_number == 2\
#     or last_number == 4\
#     or last_number == 6\
#     or last_number == 8:
#     print("짝수입니다")

# #홀수확인
# if last_number == 1\
#     or last_number == 3\
#     or last_number == 5\
#     or last_number == 7\
#     or last_number == 9:
#     print("홀수입니다")

# 리스트를 선언합니다
#딕셔너리 선언 
# foods = {"떡복이":"오뎅",
#             "짜장면":"단무지",
#             "라면":"김치",
#             "피자":"피클",
#             "맥주":"땅콩",
#             "치킨":"치킨무",
#             "삼겹살":"상추" };

#메인코드부분
# while (True) :
#     myfood = input(str(list(foods.keys())) + "중 좋아하는 음식은?")
#     if myfood in foods :
#         print("<%s>) 궁합음식은 <%s>입니다." % (myfood, foods.get(myfood)))
#     elif myfood == "끝" :
#          break
#     else :
#         print("그런 음식이 없습니다. 확인해 보세요.")
 
#  #역반복문
# for i in range(4, 0 -1 , -1):
#     print("현재 반복 변수: {}".format(i)) 

# i = 0
# while i < 10:
#     print("{}번째 반복입니다.".format(i))
#     i += 1

# 변수선언
list_test = [1, 2, 1, 2]
value = 2

#list_test 내부에 value 가있다면 반복
while value in list_test:
    list_test.remove(value)

#출력한다
print(list_test)
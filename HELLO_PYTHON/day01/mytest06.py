#홀짝을 입력하시오 ex홀
#나 : 홀
#컴 : random
#같으면 이김 다르면 짐

import random
# from secrets import choice

# num = input("홀? 짝?")

# # rnd = random()

# # com = ""

# # if rnd > 0.5:
# #     com = "홀"
# # else: 
# #     com = "짝"

# arr = ["홀","짝"]
# com = ""
# com = choice(arr)

# if num == com:
#     print("이김")
# else:
#     print("비김")

com = "" 
mine = ""
result =  ""

mine = input("홀짝?")

rnd = random.random()

if rnd > 0.5:
    com = "홀"
else:
    com = "짝"

if com == mine:
    result = "이김"
else:
    result = "짐"

print("mine",mine)
print("com",com)
print("result",result)

    
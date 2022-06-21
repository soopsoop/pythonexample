#첫수를 입력하시오 ex3
#끝수를 입력하시오 ex5
#ex 3 ~ 5의 합은 ?입니다

a = input("첫수 입력")
b = input("끝수 입력")
aa = int(a)
bb = int(b)

sum = 0

# arr = range(aa,bb+1)

# for i in arr:
#     sum+=i

for i in range(aa,bb+1):
    sum += i

print(aa,"와 ",bb,"의 합은 ",sum,"입니다.")
# print(str(aa)+"와 "+str(bb)+"의 합은 " +str(sum)+"입니다.")
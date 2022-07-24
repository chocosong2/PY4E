# 한국 나이를 미국 나이로 변환하는 프로그램

age = int(input("당신의 한국 나이를 입력해주세요"))
birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 입력 : "))

if birth == 0:
    print("미국나이:", age-1)
elif birth == -1:
    print("미국나이:", age-2)
else:
    print("0 또는 -1을 입력해주세요")

import random
n = random.randint(1, 100)
print("")
print("*****歡迎來到猜數字遊戲*****")
while True:
	a = input("請輸入1~100其中一個數:")
	a = int(a)
	if a == n:
		print("終於猜對了!")
		break
	elif a < n:
		print("比",a,"還大")
	else:
		print("比",a,"還小")
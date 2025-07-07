import random
print("")
print("*****歡迎來到猜數字遊戲*****")
start = input("請決定數字範圍開始值:")
end = input("請決定數字範圍結束值:")
start = int(start)
end = int(end)
n = random.randint(start, end)
count = 0
while True:
	count += 1 # count = count + 1
	a = input("請輸入範圍中其中一個數:")
	a = int(a)
	if a == n:
		print("**********終於猜對了!**********")
		print("這是你猜的第", count, "次")
		break
	elif a < n:
		print("答案比", a, "還大")
	else:
		print("答案比", a, "還小")
	print("這是你猜的第", count, "次")
# Given number is divisible by 3 or not

num = int(input("Enter your number:"))

if num%3==0 and num%6==0:
	print("The number is divisble by 3 and 6")
elif num%3==0:
	print("The number is divisble by 3")
elif num%6==0:
	print("The number is divisble by 6")
else:
	print("The number is not divisble by 3 or by 6")
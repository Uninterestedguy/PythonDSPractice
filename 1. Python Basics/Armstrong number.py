# Given number is armstrong or not

num = int(input("Enter your number:"))

digits = [int(i) for i in str(num)]
sum = 0 
for i in digits:
	sum=sum+(i**3)

if(sum==num):
	print("Given number is armstrong")
else:
	print("Given number is not armstrong")
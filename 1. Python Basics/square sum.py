# Addition of squares of indiviual digits
num = int(input("Enter your Number:"))

digits = [int(i) for i in str(num)]
sum = 0 
for i in digits:
	sum=sum+(i**2)

print("The sum of squares of digits of num {} is {}".format(num,sum))
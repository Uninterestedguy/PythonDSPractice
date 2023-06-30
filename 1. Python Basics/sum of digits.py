val = int(input("Enter a number"))
sum=0
while(val!=0):
	x=val%10
	sum=sum+x
	val=int(val/10)
print(sum)
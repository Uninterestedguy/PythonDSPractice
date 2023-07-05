# Check the prime numbers between given number from 0

num = int(input("Enter your number: "))
count = False
for i in range(num+1):
	if(i<=1):
		print("There are no primes")
		break
	if(i>1):
		for j in range(int(i/2)):
			if(i%j==0 and j>1):
				count = True
	if(count):
		print("{} is a prime".format(i))
		count = False

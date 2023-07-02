# Finding the palindrome of a number
first = int(input("Enter your number"))
str_first = str(first)
rev_first = str_first[::-1]
second = int(rev_first)
if(first == second):
	print("{} is a palindrome".format(first))
else:
	print("{} is not a palindrome".format(first))
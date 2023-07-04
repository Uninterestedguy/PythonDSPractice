# Reading test file
with open("filename.txt") as file:
	data = file.readlines()

# Opening in write mode
with open("filename.txt","w") as file:
	file.write(data)

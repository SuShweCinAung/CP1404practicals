name = input("Enter your name: ")
name_file = open('name.txt' ,'w')
name_file.write(name)
name_file.close()

name_file = open('name.txt', 'r')
print("Your name is", name_file.read())
name_file.close()

num_file = open('numbers.txt', 'r')
total = 0
for i in range (2):
    number = int(num_file.readline())
    total += number
print(total)

num_file = open('numbers.txt', 'r')
print(num_file.readlines())
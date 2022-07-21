# ask user for name
name = input ('What is your name?: ') 

# ask user for age
age = input ('What is your age?: ')

# ask user for city
city = input ("Where do you live?: ")

# ask user what they enjoy
love = input ("What do you enjoy?: ")

# create output text
string = "Hello, {}? Arent you {} years old and currently living in {}? Your passion is the same as mine, {}."
output = string.format(name,age,city,love)

# print output to screen
print(output)

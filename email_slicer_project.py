#get user's email address
email_address = input("What is your user name?: ").strip()

#slice out username
user = email_address[:email_address.index("@")]

#slice domain name if you do not want the @ included
domain = (email_address[email_address.index("@") + 1:])
#format message
message = "Hello, your username is {} and your domain used is {}"
output = message.format(user,domain)
#display output message
print (output) 

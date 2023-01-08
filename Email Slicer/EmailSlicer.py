#January 3 2022: Alejandro Veloz Martinez
#This code will slice email address. 

#Get email address
#with the method strip, we make sure we get rid of spaces entered by the user.
email = input("What is your email address? : ").strip()

#Slice out user name 
user_id = email[ : email.index("@")]

#slice domain name
domain = email [email.index("@") + 1:] 
#Format message
output = "Your username is {} and your domain is {}"
#Display output message. 
message = output.format(user_id , domain)
print(message)
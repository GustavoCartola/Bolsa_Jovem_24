from random import choice
import string

password_length = int(input("Quantos dígitos você quer na sua senha? "))  # prompt for password length
characters = string.ascii_letters + string.digits  # available characters for the password
secure_password = ''
for i in range(password_length):
    secure_password += choice(characters)  # randomly select a character and add it to the password

print("A senha (segura) gerada é: ", secure_password)  # display the generated secure password

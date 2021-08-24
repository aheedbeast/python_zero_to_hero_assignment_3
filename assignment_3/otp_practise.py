import string, random

characters = list(string.digits+string.ascii_letters)

otp = ""
for i in range(6):
    otp += random.choice(characters)

print(otp)
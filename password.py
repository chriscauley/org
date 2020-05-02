import string
import random

choices = string.ascii_letters + string.digits
symbols = "!@#$"
pw = ''.join([random.choice(choices) for i in range(7)])
pw += random.choice(symbols)
pw += ''.join([random.choice(choices) for i in range(7)])
pw += random.choice(symbols)
print(pw)
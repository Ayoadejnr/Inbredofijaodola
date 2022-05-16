password = input('Create a password: ')
characters = ('!', '@', '#', '$', '%', '&', '*')
numeric = 0
symbols = 0
for letters in password:
    if letters.isnumeric():
        numeric += 1
    if letters in characters:
        symbols += 1
if len(password) >= 7 and numeric >= 2 and symbols >= 2:
    print('Strong Password')
else:
    print("""
Password must have a minimum of '2 numbers',
'2 special characters' and at least '7 characters' long
""")

# sample = input('\nEnter something: ')
# num2 = []

# for tmp_a in range(10):
#    num2.append(tmp_a)

# for tmp_b in num2:
#    if str(tmp_a) in sample:
#        print('Contains number. Please try again.')
#        break
# else:
#     print('Saving your entry...')
'''
fname = input('What\'s your firstname: ').strip().capitalize()
lname = input('Lastname: ').strip().capitalize()
email_add = input('Enter email address: ').strip()

while '@' not in email_add:
    print('Not a valid email. Please enter a valid email')
    email_add = input('Enter email address: ').strip()

pw = input('\nEnter new your password: ').strip()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U' 'V',
            'W', 'X', 'Y', 'Z']
num = '0123456789'

Var1 = 0
while Var1 == 0:
    if (
            any(pw_letter in pw for pw_letter in alphabet) and
            any(var1 in pw for var1 in num) and
            len(pw) >= 8
    ):

        print('Password successfully created.')
        length_pw = len(pw) - 1
        pw1 = '*' * length_pw


        print(f'''
         Thanks for your registration, {fname}

         Here are your registration details:

         First Name: {fname}
         Last Name: {lname}
         Email Address: {email_add}
         Password: {pw[0]}{pw1}{pw[-1]}
      ''')

        break
    else:
        print('Enter a password of at least 8 characters, one uppercase letter and one number. ')
        pw = input('\nEnter password: ').strip()
'''







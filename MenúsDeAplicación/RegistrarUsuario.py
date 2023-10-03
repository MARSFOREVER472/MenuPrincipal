main = """
WELCOME TO THE USER SIGN UP, FILL OUT THE FIELDS YOU 
PREFER BELOW BY SELECT A NUMBERS FROM 1 TO 3:

[1] INPUT YOUR NAME
[2] INPUT YOUR AGE
[3] INPUT YOUR E-MAIL

"""

print(main)

option = input('ENTER A OPTION 1 TO 3: ')

if option == '1':
    name = input('ENTER YOUR NAME: ')
    if name.isalpha():
        print('YOUR NAME IS {}'.format(name))
    
    else:
        print('INVALID PARAMETERS!!!')

elif option == '2':
    age = input('ENTER YOUR AGE: ')
    if age.isnumeric():
        print('YOUR AGE IS {}'.format(age))
    
    else:
        print('INVALID PARAMETERS!!!')

elif option == '3':
    email = input('ENTER YOUR VALID E-MAIL: ')
    if email.find('@') >= 0 and email.find('.') >= 0:
        print('YOUR EMAIL IS {}'.format(email))

    else:
        print('INVALID PARAMETERS!!!')

else:
    print('YOU MUST ENTER A NUMBER BETWEEN 1 A 3!!!')
    print('=-='* 20)
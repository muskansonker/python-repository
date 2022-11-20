username=input("Enter Username: ")
email=input("Enter Email: ")
pwd=input("Enter password: ")
cpwd=input("Confirm password:")

if len(username)>0 and username.isalnum():
    if len(email)>0 and '@' in email:
       # print('Email and Username are valid')
        if len(pwd)>=4:
            if pwd==cpwd:
                print('Registration successfull')
            else:
                print('Passwords do not match')
        else:
            print('Password must be atleast 4 characters')
    else:
        print('Invalid email')
else:
    print('username is invalid')

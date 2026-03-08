import re
#define an input
password = input("Enter your password :")
count= 0

#lengty check
if len(password )>=8:
    count +=1
#numbers
if re.search(r"\d",password ):
    count +=1
#uppercase letter
if re.search(r"[A-Z]",password):
    count +=1

#special ch
if re.search(r"[!@#$%^&(),.?\":{}|<>]",password ):
    count+=1

#result
if count <=1:
    print("Weak password!")
elif count ==2:
    print("Medium password!")
else:
    print("Strong password!")
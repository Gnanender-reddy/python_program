from pip._vendor.distlib.compat import raw_input
import re
import datetime

txt="Hello <<name>>, We have your full name as <<full name>> in our system. your contact number is 91-xxxxxxxxxx. " \
    "Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016. "
name=str (input("please provide your name: ")) #asking user to provide name.

if not name.isalpha(): #checking provided name is in alphabets or not.
    name = str(input("please provide your name in alphabets: "))
result= re.sub("<<name>>",name,txt) #substituting name with <<name>> in txt.



fullname=str(input("please provide your full name: ")) #asking user to provide full name.
if not fullname.isalpha():
    fullname = str(input("please provide your full name in alphabets: "))
result=re.sub("<<full name>>",fullname,result) #substituting full name with <<full name>>


num=input("enter your mobile number: ") #asking user to provide mobile number
if not num.isnumeric(): #checking provided number is in numeric or not.
    num=input("enter your mobile number in numerics: ")
result=re.sub("91-xxxxxxxxxx",num,result)

d=datetime.date.today() #inbuilt function for providing current date
replace=str(d)
result=re.sub("01/01/2016",replace,result) #substituting replace with "01/01/2016".
print(result) #printing result











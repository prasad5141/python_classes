#Break, Continue and PASS

# l = ['sai', 'prasad', 'kiran','prabhu', 'ale', 'kumar']

# for i in l:
#     if i == 'kiran':
#         print("I found him")
#         break
#         print("his name is", i)
#     print(i, "good guy")


# l = ['sai', 'prasad', 'kiran','prabhu', 'ale', 'kumar']

# for i in l:
#     if i == 'kiran':
#         continue
#     print(i,"package delivered")


#USAGE of False
# user_subscription_status = False

# if user_subscription_status:
#     pass
# else:
#     print("Ask user to take subscription")

#Functions
#Code Re-usage
#Order Related
#Money
#Forgot Password
#Offers & Promotionals Mails

#To send and Email we have to write 10 lines of code
#40

#one function to send email

#Write Once - Use Many

#There are Two sections in Functions
#1. Defining Function
#2. Calling the Function

# def greetings():
#     print("Hi Good Morning")

# greetings()
# greetings()

# def send_email():
#     print("sending email")
#     # print("sent")
#     return False

# email_status = send_email()
# if email_status == False:
#     send_email()

# def sum(a, b):
#     print(a, "this is a")
#     print(b, "this is b")
#     return a+b

# result = sum(20,11)
# print(result)

# def person(name, mobile_numebr, age=18):
#     print('Hi, my name is {0},my age is {1} and this is my mobile number {2}'.format(name, age, mobile_numebr))

# person(mobile_numebr=98796972728, name='sai')

#Positional Arguments
#Keyword Arguments
#Default Arguments
#Variable Length Arguments
#Keyword Variable Length Arguments


def sum(**list_of_numbers):
    print(list_of_numbers)
    print(type(list_of_numbers))
    result = 0
    for key, value in list_of_numbers.items():
        # print(key)
        # print(value)
        result += value
    return result


result = sum(a=4,b=5,c=6,d=7,e=8,f=9,t=9,z=9,g=65)
print(result)

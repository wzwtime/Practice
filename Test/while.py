# coding= utf-8
'''
'''
message = raw_input("Tell me something,and I will repeat it back to you: ") #python 2.7用raw_input()
print (message)

name = raw_input("Please enter your name: ")
print ("Hello, " + name + "!")
'''
prompt = "If you tell us who you are,we can personalize the message you see."
prompt += "\nWhat is your first name? "
name = raw_input(prompt)
print (name)

age = raw_input("How old are you? ")
age = int(age)
print (age )

height = raw_input("How tall are you,in inches? ")
height = int(height)

if height >= 36:
    print ("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

number = raw_input("Enter a number,and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print ("\nThe number " + str(number) + " is enen.")
else :
    print ("\nThe number " + str(number) + " is odd.")

#7-1 汽车租赁
car = raw_input("What's car do you want to rent?")
print ("Let me see if I can find you a " + car.title())

# 7-2 餐馆订位
person_number = raw_input("Hom much people to eat in total? ")
person_number = int(person_number)

if person_number >= 8:
    print ("There are not empty desk")
else :
    print ("There are empty desks.")

# 7-3 10的整倍数
time_10 = raw_input("Plese input a number,I'll judge if it is the times of 10. ")
time_10 = int(time_10)

if time_10 % 10 == 0:
    print ("The number " + str(time_10) + " is times of 10.")
else:
    print ("The number " + str(time_10) + " not times of 10.")

current_number = 1
while current_number <= 5:
    print (current_number)
    current_number +=1

prompt = "\nTell me something,and I will repeat it back to you:"  #prompt:提示
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = raw_input(prompt)
    if message != 'quit':
        print (message)

# 使用标志
prompt = "\nTell me something,and I will repeat it back to you:"  #prompt:提示
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = raw_input(prompt)

    if message == 'quit':
        active = False
    else:
        print (message)

prompt = "\nPlease enter the name of a city you have visited:"  #prompt:提示
prompt += "\n(Enter 'quit' when you are finished.)"

    city = raw_input(prompt)

    if city == 'quit':
        break
    else:
        print ("I'd love to go to " + str(city).title() + "!")

 # 1-10的奇数
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue    #返回循环开头 跳过下面的语句
    print (current_number)

# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice','brain','candace']
confirmed_users = []

#验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print ("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# 显示所有已验证的用户
print ("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print (confirmed_user.title())

pets = ['dog','cat','dog','goldfish','rabbit','cat']
print (pets)

while 'cat' in pets:
    pets.remove('cat')

print (pets)

responses = {}

# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = raw_input("\nWhat is your name? ")
    response = raw_input("Which mountain would you like to climb someday? ")

    # 将答卷存储在字典中
    responses[name] = response

    # 看看是否还有人要参与调查
    repeat = raw_input("Would you like to let another person respond?(yes/ no) ")
    if repeat == 'no':
        polling_active = False

# 调出结束，显示结果
print ("\n -----Poll Results-----")
for name,response in responses.items():
    print (name.title() + " would like to climb " + response + ".")

# 7-8 熟食店
sandwich_orders = ['potato','tomato','apple']
finished_sandwiches = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print ("I made your " + sandwich_order + " sandwich.")
    finished_sandwiches.append(sandwich_order)

print (finished_sandwiches)
'''

























#coding=utf-8
""""
cars=['audi','bmw','subaru','toyota']

for car in cars:
    if car=='bmw':
        print (car.upper())
    else:
        print (car.title())

answer=17
if answer!=42:
    print ("That is not the correct answer.Please try again!")

banned_users=['zhangsan','lisi','wanger']
user ='zhaowu'

if user not in banned_users:
    print (user.title()+",you can post a reponse if you wish.")

game_active=True    #布尔表达式
can_edit=False

print  game_active

#5-1条件测试
car='bmw'
print ("Is car == 'bmw'? I predict True.")
print (car=='bmw')

print ("\nIs car == 'audi'? I predict False.")
print (car=='audi')

#5-2更多的条件测试
str='hello'
str1='Hello'

print (str==str1)
print (str==str1.lower())
num=6
num1=8
print (num==num1)
print (num !=num1)
print (num > num1)
print (num < num1)
print (num >=num1)
print (num <= num1)
print (num >5 and num1 <9)
print (num >6 or num1 <8)

numbers=[1,2,3]
num=9
print (num in numbers )
print (num not in numbers)

age=17
if age>=18:
    print ("You are old enough to vote!")
else:
    print ("Sorry,you are too young to vote.")
    print ("Please register to vote as soon as you turn 18!")   #可以多行输出

age=1
if age < 4:
    print ("Your admission cost is $0.")
elif age < 18:
    print ("Your admission cost is $5.")
else:
    print ("Your admission cost is $10.")

age=12
if age < 4:
    price = 0
elif age < 18:
    price =5
else:
    price =10
print ("Your admission cost is $"+str(price)+".")

#使用多个elif代码块
age=123
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 50
print ("Your admission cost is $"+str(price)+'.')

#5-3外星人颜色#1
alien_color='green'
if alien_color=='green':
    print ("You get 5 points.")

#5-4外星人颜色#2
alien_color='green'
if alien_color=='reed':
    print ("You got 5 points.")
else:
    print ("You got 10 points.")

#5-5外星人颜色#3
alien_color='yellow'
if alien_color == 'reed':
    print ("You got 5 points.")
elif alien_color== 'green':
    print ("You got 10 points.")
else:
    print ("You got 15 points.")

#5-6人生的不同的阶段
age=65

if age < 2:
    print ("He is a baby.")
elif age < 4:
    print ("He is learning run.")
elif age < 13:
    print ("He is a chidren.")
elif age < 20:
    print ("He is a youth.")
elif age < 65:
    print ("He is a adult.")
elif age >= 65:
    print ("He is a old man.")

requested_toppings=['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':    #青椒用完了
        print ("Sorry,we are out of green peppers right now.")
    else:
        print ("Adding "+requested_topping+".")
print ("\nFinished making your pizza.")

requested_toppings=['green pipper']

if requested_toppings:
    for requested_topping in requested_toppings:
        print ("Adding "+requested_topping+'.')
    print ("\nFinished making your pizza!")
else:
    print ("Are you sure you want a plain pizza.")

#5-8 以特殊方式跟管理员打招呼
names=['admin','zhangsan','lisi','wangwu','zhaoliu']

for name in names:
    if name == 'admin':
        print ("Hello admine,would you like to see a status report?")
    else:
        print ("Hello "+name.title()+",thank you for logging in again.")

#5-9处理没有用户的情形
names=['admin','zhangsan','lisi','wangwu','zhaoliu']
names=[]
for name in names:
    if name == 'admin':
        print ("Hello admine,would you like to see a status report?")
    else:
        print ("Hello "+name.title()+",thank you for logging in again.")
if names :
      print ("")
else:
     print ("We need to find some users.")
"""
#5-10检查用户名
current_users=['Admin','zhangsan','lisi','Wangwu','zhaoliu']
new_users=['admin','zhang','Lisi','wang','zhao']

#建立新的空白列表存储小写的当前用户。
new_current_users=[]
for current_user in current_users:
    new_current_users.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in new_current_users:
        print (new_user.title()+",the user name is already used.")
    else:
        print (new_user.title()+",the user neme is not used.")



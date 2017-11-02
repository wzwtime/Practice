#coding=utf-8
'''
magicians=['alice','david','carolina']
for magician in magicians:
    print (magician.title()+",that is a greatn trick! ")
    print ("I can't wait to see you next trick,"+magician.title()+".\n")
print ("Thanks you,everyone.That was a great magic show!")  #for循环后打印的内容

#4-1比萨
fruits=['apple','banana','peach','grape']
for fruit in fruits:
    print ("I like eat "+fruit.title()+".")
print ("\nI'm very like eating banana!")

#4-2动物
animals=['dog','cat','tiger','lion']
for animal in animals:
    print ("A "+animal+" would make a great pet.")
print ("\nAny of these animals would make a great pet!")

for value in range(1,6):    #创建数值列表用range(1,6)生成1、2、3、4、5五个数
    print (value)
numbers=list(range(1,6))     #创建数字列表
print (numbers)

even_numbers=list(range(2,11,2))    #range()指定步长从2开始不断+2
print (even_numbers)

squares=[]
for value in range(1,11):
    #square=value**2     #**表示乘方，如2**5=2的5次方
    squares.append(value**2)
print (squares)

digits=[1,2,3,4,5,6,7,8,9,10]
#统计计算
print (max(digits))     #求最大值
print (min(digits))     #求最小值
print (sum(digits ))    #求和

#列表解析
squares=[value**2 for value in range(1,11)]
print (squares)

#4-3数到20
for number in range(1,21):
    print (number)

#4-4一百万
numbers=list(range(1,1001))     #用list()产生数值列表 ctr+c 终止输出
for number in numbers:
    print (number)

#4-5计算1-1000，000的总和
numbers=list(range(1,1000001))
print (min(numbers))
print (max(numbers))
print (sum(numbers))

#4-6奇数
odd_numbers=list(range(1,21,2))
for odd_number in odd_numbers:
    print (odd_number)

#4-7 3的倍数
three_times=list(range(3,31,3))
for three_time in three_times:
    print (three_time)

#4-8立方
cubes=list(range(1,11))
for cube in cubes:
    print (cube**3)

#4-9立方解析
cubes=[value**3 for value in range(1,11)]
print (cubes)

players=['charles','martina','michael','florence','eli']
print (players[0:3])    #切片指明头尾索引冒号隔开
print (players[:3])     #默认从头开始切片
print (players[3:])     #默认到尾结束切片
print (players[-3:])    #输出最后三个元素

#遍历切片
players=['charles','martina','michael','florence','eli']
print ("Here are the first three players on my team:")
for player in players[:3]:
    print (player.title())

players=['charles','martina','michael','florence','eli']
new_players=players[:]  #复制列表
print (new_players)

#4-10切片
players=['charles','martina','michael','florence','eli']
print ("The origial list are：")
print (players)
print ("\nThe first three iterms in the list are:")
print (players[:3])
print ("\nThree iterms from the middle of the list are：")
print (players[1:4])
print ("\nThe last three iterms in the list are:")
print (players[-3:])

#你的比萨和我的比萨
fruits=['apple','banana','peach','grape']
friend_fruits=fruits[:]
fruits.append('tomato')
friend_fruits.append('potato')
print ("My favorite fruits are:")
for fruit in fruits:
    print (fruit)
print ("\nMy friend's favorite fruits are:")
for friend_fruit  in friend_fruits:
    print (friend_fruit )
'''
#使用多个循环
fruits = ['apple', 'banana', 'peach', 'grape']
for fruit in fruits:
    print (fruit.title())
#coding=utf-8
#字典
'''
alien_1={'color':'green','point':5}     #大括号

print (alien_1['color'])        #通过字典名中括号键名访问值
print (alien_1['point'])

alien_1['x_point']=0        #添加键值对
alien_1['y_point']=25

print (alien_1)

alien_1={'color':'green'}
print (alien_1)
alien_1['color']='yellow'   #修改字典中的值
print (alien_1)

alien_1 = {'x_point':0,'y_point':25,'speed':'medium'}
print ("Original x-point: " + str(alien_1['x_point']))

#向右移动外星人
#根据外星认当前速度决定将其移动多远
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    #这个外星人的速速一定很快
    x_increment = 3

#新位置等于老位置加上增量
alien_1['x_point']=alien_1['x_point'] + x_increment
print ("Now x-point: " + str(alien_1['x_point']))

alien_1={'color':'green','point':5}
print (alien_1)

del alien_1['color']    #删除键值对
print (alien_1)

#6-1人
friend_infos = {'first_name':'w','last_name':'zw','age':20,'city':'hangzhou'}
print (friend_infos['first_name'])
print (friend_infos['last_name'])
print (friend_infos['age'])
print (friend_infos['city'])

#6-2喜欢的数字
like_numbers = {'zhangsan':8,'lisi':5,'wanger':9,'zhaowu':7}
print ("Zhangsan's like number is " + str(like_numbers['zhangsan']) + '.')
print ("Lisi's like number is " + str(like_numbers['lisi']) + '.')
print ("Wanger's like number is " + str(like_numbers['wanger']) + '.')
print ("Zhaowu's like number is " + str(like_numbers['zhaowu']) + '.')

#6-3词汇表
vocabulary = {'list':'列表','dictionaries':'字典','tuple':'元组'}
print ("List: " + str(vocabulary['list']))
print ("Dictionaries: " + str(vocabulary['dictionaries']))
print ("Tuple: " + str(vocabulary['tuple']))

vocabulary = {'list':'列表','dictionaries':'字典','tuple':'元组'}
for key,value in vocabulary.items():   #遍历所有键值对
    print ("\nKey: " + key)
    print ("\nValue: " + value)

vocabulary = {'list':'列表','dictionaries':'字典','tuple':'元组'}
for key in vocabulary.keys():   #遍历所有键
    print (key)

for value in vocabulary.values():
    print (value)       #遍历所有值

#每个人喜欢的语言
favorite_language={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
    }
print ("The following language have been mentioned:")
for language in set(favorite_language.values()):    #剔除重复项 使用set()集合
    print (language.title())

#6-4词汇表2
vocabulary = {'list':'列表','dictionaries':'字典','tuple':'元组'}
vocabulary['set']='集合'

for word , meaning in vocabulary.items():
    print (word.title() + " : " + meaning)

#6-5河流
river_country={'nile':'egypt','yangtze river':'china','mississippi':'america'}

for river , country in river_country.items():
    print ("The " + river.title() + " runs through " + country.title() + ".")

#6-6调查
favorite_language={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
    }
names=['jen','phil','john','tom']

for name in names:
    if name in favorite_language.keys():
        print (name.title() + " Thangks!\n")
    else:
        print ("I'am sincerely invite you to involve in the investigation.")

alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens=[alien_0,alien_1,alien_2]    #字典列表

for alien in aliens:
    print (alien)

# 创建一个用于存储外星人的空列表
aliens = []

# 创建30个绿色的外星人
for alien_number in range(30):  #0到29 共30个数即循环30次
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

#修改前三个外星人
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# 显示前五个外星人
for alien in aliens[:5]:
    print (alien)
print ("....")
# 显示创建了多少个外星人
print ("Total number of aliens: " + str(len(aliens)))

# 存储所点比萨的信息
pizza = {
    'crust': 'thick',   # crtst: 外皮
    'toppings': ['mushroons','extra cheese'],   # toppings: 配料 cheese： 奶酪 mushroons： 香菇
    }

# 概述所点的比萨
print ("You ordered a " + pizza['crust'] + "-crust pizza " +
       "with the following toppings:")

for topping in pizza['toppings']:
    print ("\t" + topping)

favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
    }
for name,languages in favorite_languages.items():
    print ("\n" + name.title() + "'s favorite language are:")
    for language in languages:
        print ("\t" + language .title())

users = {
    'aeinstein':{
        'first':'albert',
        'last': 'einstein',
        'location': 'princeton'
        },
    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
        },
    }

for username,user_info in users.items():
    print ("\nUsername: " + username)
    full_name = user_info['first'] + " " +  user_info['last']
    location = user_info['location']

    print ("\tFull name: " + full_name.title())
    print ("\tLocation: " + location.title())

# 6-7 人 字典列表
xiatian_infos = {'first_name':'xia','last_name':'tian','age':20,'city':'hangzhou'}
tangrixin_infos = {'first_name':'tang','last_name':'rixin','age':25,'city':'hangzhou'}
my_infos = {'first_name':'wu','last_name':'zhiwei','age':23,'city':'hangzhou'}

people = [xiatian_infos,tangrixin_infos,my_infos]
for info in people:
    #print (info)
    for key,value in info.items():
        print (key + " " + str(value))
    print ("\n")

# 6-8 宠物    字典列表
dog = {'type':'animal','host_name':'xiatian'}
cat = {'type':'animal','host_name': 'tang'}
cloth_dolls ={'type':'cloth_dolls','host_name':'yang'}

pets = [dog,cat,cloth_dolls]

for pet in pets:
    for type,host_name in pet.items():
        print (type.title() + " " + host_name.title())
    print ("\n")

# 6-9 喜欢的地方 列表字典
favorite_places = {
    'xiatian': ['西湖','千岛湖','九寨沟'],
    'tang': ['黄鹤楼','云台山','桂林山水'],
    'yang': ['天安门','天坛','故宫'],
    }
for name,places in favorite_places.items():
    print (name.title())
    for place in places:
        print (place)
    print ("\n")

# 6-10 喜欢的数字 列表字典
like_numbers = {
    'zhangsan': [8,5,9],
    'lisi': [5,6,8],
    'wanger': [9,8],
    'zhaowu': [7,2],
    }
for name,numbers in like_numbers.items():
    print (name.title())
    for number in numbers:
        print (number)
    print ("\n")

#6-11 城市    字典的字典
cities = {
    'beijing': {'country':'china','population':'2171万人','fact':'capital'},
    'tokyo': {'country':'japan','population':'1350.73万人','fact':'capital'},
    'new york': {'country':'america','population':'833.67万人','fact':'united nations'},
    }
for city,infos in cities.items():
    print (city.title())
    #for value in infos.values():
        #print (value.title())
    print (infos['country'].title() + " " + infos['population'] + " " + infos['fact'].title()) #指定键访问值
    print ("\n")
'''

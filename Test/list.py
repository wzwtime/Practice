#coding=utf-8   添加中文注释用
'''
bicycles=['trek','cannondale','redine','specialized']
print bicycles[0]   #访问元素 指定索引 只返回元素不包括方括号和引号
print bicycles[0].title()
print bicycles[-1].title()      #访问最后一个元素
print bicycles[-2].title()      #访问倒数第二个元素

message="My first bicycle was a "+bicycles[0].title()+"."
print message

#3-1姓名
names=['wzw','mjy','wsj','wjj','gwl','zhy','dcz','wyq']
for name in names:
    print name

#3-2问候语
names=['wzw','mjy','wsj','wjj','gwl','zhy','dcz','wyq']
for name in names:
    message=name.title()+" hello,nice to meet you!"
    print message

#3-3自己的列表
commutings=['bicycle','car','walk','train','airplane']
for communte in commutings:
    message='I would like to own a '+communte.title()+'.'
    print message

names=['wzw','mjy','wsj','wjj','gwl','zhy','dcz','wyq']
names[0]="new_wzw"      #修改列表元素
print names[-8]

#添加列表元素用append()方法
fruits=['apple','banana','peach','watermaelon']
fruits.append('arange')     #在列表末尾添加
fruits.insert(-0,'tomato')   #在列表中插入元素用insert(int index,value)方法
print fruits

fruits=['apple','banana','peach','watermaelon']
del fruits[0]   #永久性删除
print fruits

fruits=['apple','banana','peach','watermaelon']
fruits.pop()      #使用pop()方法弹出列表末尾元素
fruits.pop(2)     #指定索引弹出元素
fruits.remove('apple') #根据值删除元素,只删除第一个指定的值 后边重复的没删除
print fruits

#3-4嘉宾名单
guest_names=['sun qifan','jin zhengwei','ma junying','wu yanqing']
for guest_name in guest_names:
    message=guest_name.title()+",it's my great honor welcome you to have dineer with me."
    print message

#3-5修改嘉宾名单
guest_names=['sun qifan','jin zhengwei','ma junying','wu yanqing']
print guest_names[-1].title()+" can't coming!"
guest_names[-1]='xia tian'
for guest_name in guest_names:
    message=guest_name.title()+",it's my great honor welcome you to have dineer with me."
    print message
#3-6
print "I find a more bigger desk!"
guest_names.insert(0,'wu qing')
guest_names.insert(2,'zhang xin')
guest_names.append('wei xingming')
for guest_name in guest_names:
    message=guest_name.title()+",it's my great honor invite you to have dineer with me."
    print message

#3-7缩减名单
guest_names=['sun qifan','jin zhengwei','ma junying','wu yanqing']
print("Sorry! the new desk can't sending now.So only two guests can invite coming.")

message=guest_names.pop().title()+",sorry I can't invite you have dinner with me."
print (message)
message=guest_names.pop().title()+",sorry I can't invite you have dinner with me."
print (message)

message=guest_names[0].title()+",waiting for your coming!"
print (message)
message=guest_names[1].title()+",waiting for your coming!"
print (message)
del guest_names[0]
del guest_names[0]
print guest_names

age=20
message="I'm "+str(age)+" years old."
print (message)
'''
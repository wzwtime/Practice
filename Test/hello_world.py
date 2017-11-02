# coding=utf-8 UTF-8（8-bit Unicode Transformation Format）是一种针对Unicode的可变长度字符编码，又称万国码
# 或者是coding=gbk(GBK全称《汉字内码扩展规范》)

'''  #多行注释
message="Hello Python world!"
print(message)
message="Hello Python Crash Course world!"  #变量重新赋值
print(message)
message='This is a string.'
print (message)
message="This is also a string."
print (message)
message='I told my friend,"Python is my favorite language!"'
print (message)
message="The language 'Python' is named after Monty Python,not the snake."
print (message)
message="One of Python's strength is its diverse and supportive community."
print (message)

# 使用方法修改字符串的大小写 title():首字母大写   upper():全部大写    lower():全部小写
name="wzw"
print(name.title())
print(name.upper())
print(name)
print(name.lower())

first_name="ada"
last_name="lovelace"
full_name=first_name+" "+last_name
print ("Hello, "+full_name.title()+"!")     #字符串拼接

print ("Languages:\n\tPython\n\tC\n\tJavaScript")     #制表符的使用 \t \n

#删除空白
favorite_luangusge=" python "
print("ok_"+favorite_luangusge.lstrip().rstrip()+"_ok")       #临时去空格
favorite_luangusge=favorite_luangusge.strip()         #永久去空格
print(favorite_luangusge)

name="eric"
message="Hello "+name.title()+",would you like to learn some Python today?"
print message.lower().upper().title()

message='Albert Einstein once said,"A person who never made a mistake never tried anything new."'
print message
#拼接练习
famous_person="Albert Einstein"
famous_said='"A person who never made a mistake never tried anything new."'
message=famous_person+" once said,"+famous_said
print message

name="  tom  john   "
print (name.lstrip()+"\n")
print "\t"+name.rstrip()

print 3/2.0
print 3**3  #**：表示乘方即3*3*3
print 10**5
print 3.0+3*5
print 0.1+0.2
print 3*0.1

age=23
message="Happy "+str(age)+"rd Birthday!"
print message
'''
import this

#coding=gbk
#元组tuple
'''
dimensions=(200,50)     #元组的创建
print (dimensions[0])  #访问
print (dimensions[1])
for dimension in dimensions:    #遍历元组的所有值
    print (dimension)
dimensions=(10,20)
for dimension in dimensions:
    print (dimension)
'''
#4-13自助餐
foods=('fish','chicken','beef','apple','banana')
for  food in foods:
    print (food)
#foods[0]='pig' 不能修改元组
print ("************")
foods=('fish','chicken','beef','potato','tomato')
for food in foods[-2:]:     #根列表一样，用切片访问元组的最后两个元素
    print (food)




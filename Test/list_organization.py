#coding=utf-8 or coding=GBK
"""
cars=['bmw','audi','toyota','subaru']
cars.sort()     #默认按首字母递增排序，永久性的，不可恢复
print (cars)
cars.sort(reverse=True )    #按字母顺序相反的顺序排列 即递减排序
print (cars)

print ("Here is the original list:")
print (cars)

print ("\nHere is the sorted list:")
print (sorted(cars))    #临时排序不改变原列表元素顺序

print ("\nHere is the original list again:")
print (cars)

cars=['bmw','audi','toyota','subaru']
cars.reverse()      #反转列表元素的排列顺序
print (cars)

length=len(cars)    #确定列表的长度
print (length)

#3-8放眼世界
like_tourists=['New York','London','Tokyo','Hong Kong','Peking']
print (like_tourists)
print ("\n")
print (sorted(like_tourists))
print ("\n")
print (like_tourists)
print ("\n")
print (sorted(like_tourists,reverse=True))
print ("\n")
print (like_tourists)
print ("\n")
like_tourists.reverse()
print (like_tourists)
#print (like_tourists.reverse())     #打印的是None
print ("\n")
like_tourists.reverse()
print (like_tourists)
print ("\n***********")
like_tourists.sort()
print (like_tourists)
print ("\n***********")
like_tourists.sort(reverse=True)
print (like_tourists)

#3-9晚餐嘉宾
guest_names=['sun qifan','jin zhengwei','ma junying','wu yanqing']
message="There are "+str(len(guest_names))+" guests in total have dineer with me."
print (message)
"""

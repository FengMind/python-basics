##############################################
#  Title: 列表
#  Author: FengMind <枫鸽>
#  Email: FengMind@qq.com
#  Date: 2019-2-18
##############################################

# 1、函数list
a = list('Hello')
b = ''.join(a)
print("1、函数list:\na:%s\nb:%s\n" % (a, b))

# 2、删除元素
a = ['zhao', 'qian', 'sun', 'li', 'zhou']
del a[1]
print("2、删除:\na:%s\n" % (a))

# 3、给切片赋值
a = ['zhao', 'qian', 'sun', 'li', 'zhou']
a[2:] = ['wu', 'zhen', 'wang']
# 通过切片改变列表长度
b = list('Park')
b[1:] = list('ython')
# 替换”了一个空切片，相当于插入了一个序列
c = [1, 5]
c[1:1] = [2, 3, 4]
# 相反则删除
d = [1, 2, 3, 4, 5]
d[1:4] = []
print("3、切片赋值:\na:%s\nb:%s\nc:%s\nd:%s\n" % (a, b, c, d))

# 4、列表方法
# append
a = [1,2,3]
a.append(4)
print("append a:%s"%(a))
# clear
a=[1,2,3]
a.clear()
print("clear a:%s"%(a))
# copy
a=[1,2,3]
b=a #直接复制传递是地址
b[1]=4
# print("浅拷贝，地址传递 a:%s"%(a))
a=[1,2,3]
b=a.copy()
b[1]=4
print("copy深拷贝，值传递 a:%s,b:%s"%(a,b))
# count
a=['How','do','you','do']
count1=a.count('do')
a=[1,2,[1,2],1,[1,2,[1,2]]]
count2=a.count(1)
count3=a.count([1,2])
print("count count1:%s,count2:%s,count3:%s"%(count1,count2,count3))
# extend
a=[1,2,3]
b=[4,5,6]
a.extend(b) # equal: a[len(a):]=b
print("extend a:%s"%(a))
# index
a=['zhang','li','wang','lv','cheng']
b=a.index('lv')
print("index b:%s"%(b))
# insert
a=[1,2,3,4,5,6]
a.insert(3,'zhang') # equal: a[3:3]=['zhang']
print("index a:%s"%(a))
# pop
a=[1,2,3,4,5,6]
a.pop()
print("pop() a:%s"%(a))
a.pop(0)
print("pop(0) a:%s"%(a))
# 延伸：实现LIFO（栈Stack）  FIFO（队列）
a=[1,2,3,4,5,6]
a.append(7)
a.pop()
print("LIFO a:%s"%(a))
a=[2,3,4,5,6,7]
a.insert(0,1)
a.pop()
print("FIFO a:%s"%(a))
# 当然使用a.pop(0)的方式也可实现相反操作
# remove
a=['zhang','li','wang','lv','cheng']
a.remove('zhang')
print("remove a:%s"%(a))
# reverse
a=[1,2,3,4,5,6]
a.reverse()
print("reverse a:%s"%(a))
# sort - asc
a=[6,3,1,4,2,5]
a.sort() # 就地升序，并非副本
print("sort a:%s"%(a))
b=a.sort() # 这样做是无意义的
print("sort b:%s"%(b))
b=a # 地址传递也并非我们所愿
print("sort b:%s"%(b))
a=[6,3,1,4,2,5]
b=a.copy() # 深copy一份
b.sort()
print("sort a:%s,b:%s"%(a,b))
# sorted 副本排序
a=[6,3,1,4,2,5]
b=sorted(a) # 实现copy并对副本排序
print("sort a:%s,b:%s"%(a,b))
a=sorted('Python') # 可用于任何序列，但总是返回一个列表
print("sorted作用于任意序列 a:%s"%(a))

# sort - desc
# 使用reverse()就行







##############################################
#  Title: 序列的通用操作
#  Author: FengMind <枫鸽>
#  Email: FengMind@qq.com
#  Date: 2019-2-18
##############################################

# 1、索引 (indexing)
x = 'Hello'
a = x[0]
b = x[-1]
print("1、索引\na:%s\nb:%s\n" % (a, b))

# 2、切片 (slicing)
# desc: 第一个索引是包含的第一个元素的编号，但第二个索引是切片后余下的第一个元素的编号
#       第二个索引也可以理解为截取到从1开始算的第几个
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = nums[0:3]  # [1, 2, 3]
b = nums[5:-1]  # [6, 7, 8, 9]
# 简写
c = nums[7:10]
d = nums[7:-1]
e = nums[7:]
f = nums[:3]
g = nums[:]
print("2、切片\na:%s\nb:%s\nc:%s\nd:%s\ne:%s\nf:%s\ng:%s\n" % (a, b, c, d, e, f, g))
# 步长
h=nums[0:10:2]
i=nums[::4]
j=nums[0:10:-2]
print("2、切片\nh:%s\ni:%s\nj:%s\n" % (h, i, j))

# 3、相加 - 拼接 (add)
a = [1, 2, 3] + [4, 5, 6]
b = 'Hello,' + 'world!'
# c=[1, 2, 3] + 'world!'  # 不能拼接列表和字符串
print("3、相加\na:%s\nb:%s\n" % (a, b))

# 4、乘法 (multiple)
a = 'python' * 5
b = [1] * 10
print("4、乘法\na:%s\nb:%s\n" % (a, b))

# 5、成员资格
a = 'H' in 'Hello'
b = 'zhang' in ['zhang', 'qian', 'sun', 'li']
print("5、成员资格\na:%s\nb:%s\n" % (a, b))
# 现在可使用运算符in来检查指定的字符串是否为另一个字符串的子串
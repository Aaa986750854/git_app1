#成员运算符 in 、not in
l=[1,2,3]
ll =[1,2,3]
print (2 in l)

#身份运算符 is 、not is
print (l == ll)
print (l is ll)
print (id(l))  #id() 函数用于获取对象的内存地址。
print (id(ll))

a1=9
b1=9
print("****")
#在Python中，整数和短小的字符，Python都会缓存这些对象，以便重复使用。

print(a1==b1)
print(a1 is b1)

#左移和右移
a=4
print (bin(a)) #bin() 返回一个整数 int 或者长整数 long int 的二进制表示
print (a<<2)
print (a>>2)

#变量
print ("变量")
a = 'ABC'
b = a
a = 'XYZ'
print(b)

if(True):
    print ('OK')
else :
    print ('not ok')

def conditions():
    #str='kevin'
    
    i = 10;
    n = int(input("enter a number:"))

    if n == i:
        print ("equal")
    elif n < i:
        print ("lower")
    else:
        print ("higher")

def loop1():
    for i in range(0, 10,2):
        print (i)
    else:
        pass

def loop2():
    count=5
    while count>0:
        print (count)
        count=count-1
    else:
        print ('over')
        
def var():
    i=0
    mystr='hello python' 
    mystr2="hello"
    a = b = c = 1
    d, e, f = 1, 2, "john"
    
    #列表是可变的有序表复合数据类型
    mylist = [ 'abcd', 786 , 2.23, 'john', 70.2 ]

   
    #元组是类似于列表中的序列数据类型,但是tuple初始化就不能修改
    mytuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )

    
    
    #字典
    mydict = {'name': 'john','code':6734, 'dept': 'sales'}
    
    print (mystr[0] ) #第一个元素
    print (mystr * 2)   #字符串内容*2

    mylist.append('test')
    print (mylist)
    print (mylist[1:]) #第一个元素到最后一个
    print (mylist[-1])  # 最后一个元素
    mylist[2] = 1000
    print (mylist[2])


    print (mytuple[2:4]) #第二个元素和第四个元素之间，不包括第四个元素
    #tuple[2] = 1000  #元组不能改变，元组内数值的大小
    print (mytuple[2])
    print (mydict)
    print (mydict['name'])
    print (mydict.values())
    
    for i in mylist:
        print (i)
    else:
        pass
    


if __name__ == '__main__':
    #conditions()
    #loop1()
    #loop2()
    var()



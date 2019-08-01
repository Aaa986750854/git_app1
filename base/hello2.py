import os
import selenium

print ('hello2')

a=1
b=123.5
c="Sssss".count('s')
d='jlkjklj'
print(d.find('i'))
print ("ABC".lower())

l=['1','2',2222,'aaa']
print ('*****')
print (l[1])
print (l[-1])
print ('c的s字符个数',c)

print(l[0])
print(l[1])
print(l.__len__())
print(l.append('444444'))
l.remove('2')

print(len(l))
print(l)

ll=[1,2,[33,3],4]
print(ll)
print(len(ll))


classmates = ('Michael', 'Bob', 'Tracy')

print('******')
print(classmates.index('Bob'))
print(classmates)

t = ('a', 'b', ['A', 'B'])
print(id(t))
print(id(t[2]))
print(id(t[2][0]))
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
print(id(t[2]))
print(id(t[2][0]))


tt = ('a', 'b', 'c')
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
print("has key:")
print(d.keys())
print(d.values())


s = set([1, 2, 3])

print (s)
s.add(4)
print (s)

s.add(3)
print (s)
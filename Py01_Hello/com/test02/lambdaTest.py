hap = lambda a,b : a + b
print(hap(1,5))

gob = lambda a,b: a * b
print(gob(4,5))
            #참이면  왼쪽 거짓이면 오른쪽
min = (lambda x , y : x if x < y else y)(10,20)
print(min)

max = (lambda x,y : x if x > y else y)
print(max(10,20))

a = [(1, 'one', 9), (2,'two',8), (3,'three' ,7), (4,'four',6)]
a.sort(key = lambda a:a[2])
print(a)

b = lambda x: (lambda newx : x + newx)
c = b(100)
print(c)
d = c(90)
print(d)
print(b(100)(90))

e = lambda x : bool(x % 5)
five = [i for i in range(1, 100) if not e(i)]
print(five)

f = lambda x : x if(x%5 != 0) else None
res = [i for i in range(1, 100) if not f(i)]
print(res)

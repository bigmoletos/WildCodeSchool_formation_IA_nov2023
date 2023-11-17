a,b = 0,1
def fibI():
 global a,b
 while True:
  a,b = b, a+b
  yield a
f=fibI()
f.next()
f.next()
f.next()
f.next()

print (f.next())

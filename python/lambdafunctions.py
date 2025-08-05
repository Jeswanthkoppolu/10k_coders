#lambda function
x=lambda: print("hello world")

x=lambda:5
print(x())

x=lambda a,b:a+b
print(x(6,2))

even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(even_odd(10))


#scope
#local
def myfunc():
  x = 300
  print(x)
myfunc()

#enclosed
def myfunc():
  x = 300
  def myinnerfunc():
    y=400
    print(y)
    print(x)
  myinnerfunc()
  print(x) 
myfunc()


#global
x= 300
def myfunc():
  print(x)
myfunc()

print(x)
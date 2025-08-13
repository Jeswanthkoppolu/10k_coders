#code-1
x=10
def show():
    x=5
    print(x)
show()
print(x) 

#Inside the function, x = 5 is local → prints 5.
#Outside the function, x = 10 is global → prints 10.
 

#code-2
def outer():
    x=100
    print(x)
    def inner():
        print(x)
    inner()
outer()

#outer() defines x = 100 and prints it.
#inner() uses x from outer() (closure) and also prints 100

#code-3
x="global"
def outer():
  x="outer"
  def inner():
      x="inner"
  inner()    
outer()
print("global",x) 
#Inner variables don’t change outer or global ones.
#x = "inner" is local to inner(), so global x stays "global". 
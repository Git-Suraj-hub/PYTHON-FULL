# def greet(fx):
#     def wrapper():
#         print("GOOD MORNING")
#         fx()
#         print("THANKS FOR USING THIS SERVICE")
#     return wrapper
def add(fx):
  def c(*args,**kwargs):
    print("CALCULATOR")
    fx(*args,**kwargs)
  return c
# @greet
# def hello():
#     print("Hello World")
@add
def add(a,b):
    print(a+b)
add(a=0,b=0)




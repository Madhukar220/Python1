# def log(func):
#     def wrapper(*args,**kwargs):
#         print(func.__name__)
#         return func(*args,**kwargs)
#     return wrapper
#
#
# @log
# def display():
#     pass
#
# display()


# def count_(func):
#     def wrapper(*args,**kwargs):
#         print(len(args)+len(kwargs))
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @count_
# def display(a,b,c,d):
#     return a+b+c+d
# print(display(10,20,30,10))

#
# import time
# def delay(fun):
#     def wrapper(*args,**kwargs):
#         time.sleep(5)
#         return fun(*args,**kwargs)
#     return wrapper
#
#
# @delay
# def display():
#     print("Hi how are you doing")
#
# display()
import time


# def exection_(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         res = func(*args,**kwargs)
#         end = time.time()
#         return start,end, end - start ,res
#
#     return wrapper
#
# @exection_
# def display():
#     return ("The execution hours is")
# print(display())


# def rep(func):
#     def wrapper(*args, **kwargs):
#       for i in range(3):
#
#         res = func(*args, **kwargs)
#         print(res)
#
#
#     return wrapper
#
# @rep
# def fun(a,b):
#     return a+b
# fun(2,8)

# count = 0
# def call(func):
#
#     def wrapper(*args,**kwargs):
#         global count
#         count= count+1
#         res = func(*args,**kwargs)
#         return count , res
#     return wrapper
# @call
# def add(a,b):
#     return a+b
# print(add(2,5))
# print(add(6,8))
#
# @call
# def sub(c,d):
#     return d-c
# print(sub(2,6))

# d = {}
# def call_count(func):
#     def wrapper(*args,**kwargs):
#        if func.__name__ not in d:
#            d[func.__name__] = 1
#        else:
#            d[func.__name__]+=1
#        res = func(*args,**kwargs)
#        return res,d
#     return wrapper
# @call_count
# def add(a,b):
#     return a+b
# print(add(2,5)
# print(add(6,8))

# @call_count
# def sub(c,d):
#     return d-c
# print(sub(2,6))

# def upper(func):
#     def wrapper(*args,**kwargs):
#         res = func(*args,**kwargs)
#         return abs(res)
#     return wrapper
#
# @upper
# def sub(a,b):
#     return a-b
# print(sub(2,6))






#####################  LAMBDA FUNCTIONS  #############


# add = lambda num: num+15
# print(add(20))

# even = lambda num: "given number is even"  if num % 2 == 0 else "the given number is odd"
# print(even(24))

# palin = lambda sequence: "the given string is pallindrome" if sequence == sequence[::-1] else "the given string is not a pallindrome"
# print (palin("MADAM"))

# returnd = lambda sequence: sequence[-1]
# print(returnd("hellol"))

# square = lambda a, b: a*b
# print(square(10,20))

######## MAP PROGRAMMES #######################

# l1 = [2, 5, 6, -2, -3, -5]
#
# def positive(l):
#     return abs(l)
# print(list(map(positive,l1)))

# l = ["hi", "its", "My", "Own", "Car"]
# def last(string):
#     if string[0] in "aeiouAEIOU":
#         return string
# print(list(map(last,l)))



# l = [1, 2, 3, 4]
# def mul(num):
#     return(num**2, num**3)
# print(list(map(mul,l)))

# l = [1, 2, 3, 4]
#
# def indecs(num):
#     index,item = num
#     return item**index
# print(list(map(indecs,enumerate(l))))

# l1 = [1, 2, 3, 4]
# l2 = [4, 5, 6, 7]
# l3= [3, 5, 8, 9]
#
# def add(a,b,c):
#     return a+b+c
# print(list(filter(add,l1,l2,l3)))


# s = "hai good afternoon"
# words = s.split()
# def case(word):
#     return word.upper()
# print(list(map(case,words)))


# l = ["hi", "its", "My", "Own", "Car"]
# def vowels(sequence):
#     if sequence[0] in "aeiouAEIOU":
#         return sequence
#
#
# print(list(filter(vowels,l)))

# i = range(1,51)
# def odd(num):
#     if num % 2 == 1:
#         return num
#
# print(list(filter(odd,i)))

# l = ["hello", "it", "is", "normal", "day"]
# def length(word):
#     if len(word) % 2 == 1:
#         return word
#
#
# print(list(filter(length,l)))

# l1 = [2, 5, 6, -2, -3, -5]
#
# def pos(num):
#     if num<0:
#         return num
#
#
# print(list(filter(pos,l1)))

#
# l = range(1,51)
#
# def prime(num):
#     if num>1:
#         for i in range(2,num):
#             if num % i == 0:
#                 break
#         else:
#             return num
#
#
# print(list(filter(prime,l)))
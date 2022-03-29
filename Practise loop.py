
# for i in range (1,11):
#    print(i , end=" ")


# for i in range(1, 51):
#     if i % 2 == 0:
#        print(i ,end= " ")


# s = "hello"
# for i in range(len(s)):
#    print(i, s[i])

# s = "HeLLo WorLd"
#
# res = ""
# for char in s:
#    if "a" <= char <= "z":
#       res = res + chr(ord(char)-32)
#    elif "A" <= char <= "Z":
#       res = res + chr(ord(char)+32)
#
#    else:
#       res = res + char
# print(res)

# s = "HeLLo WorLd"
# res= ""
# for i in s:
#      if "a" <= i <= "z":
#         res = res + chr(ord(i)-32)
#
#      elif "A" <= i <= "Z":
#         res = res + chr(ord(i)+32)
#      else:
#         res = res + i
# print(res)


# s = "hello world"
# count = 0
# for i in s:
#      count =count+1
# print(count)

# s = "how are you man iy"
# words = s.split()
# count = 0
# for word in words:
#       count = count + 1
# print(count)

# s = "hello world"
# for rep in s:
#   if s.count(rep)>1:
#      print(rep,end="")

# s = "how are you doing man"
# res = ""
# for rep in s:
#    if rep not in res:
#       res = res +rep
# print(res)

# s = "hello world"
# non_duplicates = ""
# duplicates = ""
# for i in s:
#      if i not in non_duplicates:
#        non_duplicates = non_duplicates+i
#      else:
#         duplicates = duplicates + i
# print(non_duplicates)
# print(duplicates)
#
#
# s = "helloABC"
# res = ""
# for char in s:
#    if "a" <= char <= "z":
#       res = res + chr(ord(char)-32)
#    else:
#       res = res + char
# print(res)

# s = "hello world"
# char = "l"
# for i in range(len(s)):
#    if s[i] == char:
#      print(i)

# s = "hello world"
# char = "o"
#
# for i in range(len(s)):
#     if s[i] == char:
#         print(i)
#         break

# s = "hello world"
# char = "o"
# count = 0
# for i in range(len(s)):
#    if s[i] == char:
#       count =count+ 1
#    if count == 2:
#       print(i)
#       break


# s = "hello man how are you is every thing is ok"
# words = s.split()
# for word in words:
#    if word[0] in "aeiouAEIOU":
#       print(word)

# sentence = "Today it was raining in the morning"
# words = sentence.split()
# l = []
# for word in words:
#     if len(word) % 2 == 0:
#        l.append(word)
# print(l)


# sentence = "Todai it wao raining in the morning"
# words = sentence.split()
# l = []
# for word in words:
#    if word[-1] in "aeiouAEIOU":
#       l.append(word)
#
# print(l)

# sentence = "Todai it wao raining in the morning"
# words = sentence.split()
# set_ =set()
# for word in words:
#    if word[-1] in "aeiouAEIOU":
#       set_.add(word)
#
# print(set_)
#
# sentence = "Todai it wao raining in the morning"
# words = sentence.split()
# l = []
# for word in words:
#    item = (word,len(word))
#    l.append((item))
# print(l)

# sentence = "hello welcome to the evening session of python"
# d = {}
# words = sentence.split()
# for word in words:
#    if word[0] in "aeiouAEIOU":
#       d[word] = len(word)
# print(d)

# s = "hello welcome"
# d = {}
# for i in range(len(s)):
#    if s[i] not in d:
#       d[s[i]] = [i]
#    else:
#       d[s[i]].append(i)
#
# print(d)


# d = {"a": 1, "b": "hello", "c": 25, "d": "are", "e": [1, 2, 3], "f": "you"}
# dic = {}
#
# for key, value in d.items():
#    if isinstance(value, int):
#       dic[key] = [value]
#
# print(dic)
from collections import defaultdict

# d = {"a": 1, "b": "hello", "c": 25, "d": "are", "e": [1, 2, 3], "f": "you"}
# dic = {}
#
# for key,value in d.items():
#     if isinstance(value,str):
#           dic[key] = value[::-1]
#     else:
#          dic[key] = value
# print(dic)
from itertools import zip_longest

s = "Hi how are you doing today"
# d = {}
# words = s.split()
#
# for word in words:
#       if len(word) not in d:
#             d[len(word)] = [word]
#       else:
#            d[len(word)].append(word)
# print(d)


# dd = defaultdict(list)
# words = s.split()
# for word in words:
#    dd[len(word)].append(word)
# print(dd)


# s = "hai  you hai you"
#
# words = s.split()
#
# d = {}
#
# for word in words:
#     if word not in d:
#        d[word] = 1
#     else:
#        d[word] = d[word]+1
# print(d)

# dd = defaultdict(int)
# words = s.split()
# for word in words:
#    dd[word] = dd[word]+1
#
# print(dd)
# d = {}
# words = s.split()
# for i in range(len(words)):
#    d[i]= words[i]
# print(d)
#
# for item1,item2 in enumerate(words):
#    d[item1] = item2
# print(d)

l1 = ["hai","hello","how","are"]
l2 = [1, 2,]
d = {}
# for i in range(len(l1)):
#    d[l1[i]] = l2[i]
# print(d)
#
# for item1,item2 in zip_longest(l1,l2,fillvalue="nothing"):
#    d[item1] = item2
# print(d)

# num = 59
#
# for i in range(2,num):
#    if num % i == 0:
#       print("given number is not prime")
#       break
# else:
#     print("the given number is  prime number")

# for num in range(1,10):
#    if num > 1:
#       for i in range(2,num):
#          if num % i == 0:
#
#             break
#       else:
#          print(num)


# num = 0
# count = 0
# x = 5
# while count < x:
#    if num > 1:
#       for i in range(2,num):
#          if num % i == 0:
#
#             break
#       else:
#          count = count+1
#          if count == x:
#             print(num)
#    num = num+1


# a = 0
# b = 1
# for _ in range (7):
#    print(a,end=" ")
#    c = a+b
#    a = b
#    b = c

# a = 0
# b = 1
# n = 5
# for i in range(n-1):
#    c = a+b
#    a = b
#    b = c
# print(a)


# a = 0
# b = 1
# while a<10:
#    print(a,end=" ")
#    c = a+b
#    a = b
#    b = c


# l = [10 , 95, 15, 5, 80, 60]
# for i in range(len(l)-1):
#    if l[i] > l[i+1]:
#       l[i],l[i+1] = l[i+1],l[i]
#
# print(l[0])

# l = []
# for num in range(1,11):
#
#         l.append( num * num)
# print(l)

#
# s = "hi how hi are how  you"
# words = s.split()
# count = 1
# l = []
# for word in words:
#     if word not in l:
#         l.append((word,count))
#     else:
#         count1 = count+1
#         l.append((word,count1))
# print(l)

# l = []
# fact = 1
# for num in range (1,6):
#     fact =num * fact
#     l.append(fact)
# print(l)





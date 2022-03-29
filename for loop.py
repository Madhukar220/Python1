# l= [10, 20, 30, 40]
# for item in l:
#     print(item)

# s = "hello world"
#
# for item in s:
#     print(item, end=" ")

# sentence = "hello world"
# d = {}
# for i in range(len(sentence)):
#     if sentence[i] not in d:
#         d[sentence[i]] = [i]
#     else:
#         d[sentence[i]].append(i)
#
# print(d)

# s = "how are you"
# d = {}
# for i in s:
#     d[i] = ord(i)
# print(d)

# d = {"a":1, "b":"hello","c": 85, "d":12.3, "e":[1 ,2 ,3] , "f":"world"}
#
# d1 = {}
#
# for key,value in d.items():
#     if isinstance(value,int):
#         d1[key] = value
# print(d1)

# d = {"a":1, "b":"hello","c": 85, "d":12.3, "e":[1 ,2 ,3] , "f":"world"}
#
# dic = {}
#
# for key,value in d.items():
#     if isinstance(value,str):
#         dic[key] = value[::-1]
#
#     else:
#         dic[key] = value
# print(dic)

# s = "hi how are you doing today"
#
# words = s.split()
# d = {}
# for word in words:
#     d[word] = [len(word)]
# print(d)

# for word in words:
#     if len(word) not in d:
#         d[len(word)] = [word]
#     else:
#         d[len(word)].append(word)
#
# print(d)

# from collections import defaultdict
#
# s = "hi how are you doing today"
# dd = defaultdict(list)
# words = s.split()
# for word in words:
#     dd[len(word)].append(word)
# print(dd)
from collections import defaultdict

# s = "hi how are hi are how you hi how"
#
# words = s.split()
#
# d = {}
# for word in words:
#     if word not in d:
#         d[word] = 1
#     else:
#         d[word]+= 1
# print(d)

# s = "hi how are hi are how you hi how"
#
# dd = defaultdict(int)
#
# words = s.split()
# for word in words:
#     dd[word] = dd([word]+1)

# s = "hi how  are you man"
# words = s.split()
# d = {}
# for i in range(len(words)):
#      d[i] = words[i]
#
# print(d)
from itertools import zip_longest

# l1 = "hello", "word", "how", "are"
# l2 = 10, 20
d = {}
# for i in range(len(l1)):
#     d[l1[i]] = l2[i]
# print(d)

# for item1,item2 in zip_longest(l1,l2,fillvalue="not present"):
#     d[item1] = item2
#
# print(d)



# for row in range(1,5):
#     print("* "*row)
# print()

# for row in range(4 , 0, -1):
#     print("* " * row)
# print()

# for row in range(1 ,5):
#     print(f'{"* "*row:>8}')
# print()

# for row in range(4 , 0 ,-1):
#     print(f'{"* " * row:>8}')
# print()

# for row in range(1, 5):
#     print(f'{"* "*row:^8}')
# print()

# for row in range(1,5):
#     print("*")
#     print("* "*row)
# print()


for row in range(1,5):
    for col in range(row):
        print(row,end=" ")
    print()


for row in range (1 ,5):
    ch = ord("a")
    for col in range(row):
        print(chr(ch),end=" ")
        ch+=1
    print()

for row in range(4, 0,-1):
    ch=ord("a")
    for col in range(row):
        print(chr(ch),end=" ")
        ch+=1
    print()

